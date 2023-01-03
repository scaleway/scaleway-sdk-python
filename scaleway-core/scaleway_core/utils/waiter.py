import asyncio
import inspect
import math
import random
import time
from dataclasses import dataclass
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    Generator,
    Generic,
    Optional,
    TypeVar,
    Union,
)

system_random = random.SystemRandom()

T = TypeVar("T")
U = TypeVar("U")

WaitForStopCondition = Callable[[T], U]


@dataclass
class WaitForOptions(Generic[T, U]):
    """
    The options to wait until a resource is ready.
    """

    timeout: float = 300
    """
    Timeout in seconds.

    :default: 300 seconds (5 minutes).
    """

    min_delay: float = 1
    """
    The minimum delay before the next try in seconds.

    :default: 1 second.
    """

    max_delay: float = 30
    """
    The maximum delay before the next try in seconds.

    :default: 30 seconds.
    """

    stop: Optional[WaitForStopCondition[T, U]] = None
    """
    The condition to stop trying.

    :default: Waits for non-transient value.
    """


def _exponential_backoff_strategy(
    min_delay: float,
    max_delay: float,
) -> Generator[float, None, None]:
    """
    Generates a sequence of delays using an exponential backoff strategy.

    :param min_delay: The minimum delay before the next try in seconds.
    :param max_delay: The maximum delay before the next try in seconds.
    """
    if min_delay < 1:
        raise ValueError("min_delay must be greater than 1")

    if max_delay < min_delay:
        raise ValueError("max_delay must be greater than min_delay")

    max = math.log(max_delay / min_delay) / math.log(2) + 1

    attempt = 1
    while True:
        if attempt > max:
            yield max_delay
        else:
            yield system_random.uniform(min_delay, min_delay * 2 ** (attempt - 1))

        attempt += 1


def _delayed_loop(options: WaitForOptions[Any, Any]) -> Generator[float, None, None]:
    strategy = _exponential_backoff_strategy(options.min_delay, options.max_delay)
    timeout_time = time.time() + options.timeout

    while time.time() <= timeout_time:
        delay = next(strategy)
        if timeout_time <= (time.time() + delay):
            break

        yield delay

    raise TimeoutError("Timeout while waiting for resource")


async def wait_for_resource_async(
    fetcher: Callable[..., Awaitable[T]],
    options: WaitForOptions[T, Union[bool, Awaitable[bool]]],
    args: Dict[str, Any],
) -> T:
    """
    Fetches resource several times until an expected condition is reached, timeouts, or throws an exception.
    """
    if options.stop is None:
        raise ValueError("options.stop is required")

    for delay in _delayed_loop(options):
        await asyncio.sleep(delay)

        resource = await fetcher(**args)

        should_stop = options.stop(resource)
        if inspect.isawaitable(should_stop):
            should_stop = await should_stop

        if should_stop:
            return resource

    raise TimeoutError("Timeout while waiting for resource")


def wait_for_resource(
    fetcher: Callable[..., T],
    options: WaitForOptions[T, bool],
    args: Dict[str, Any],
) -> T:
    """
    Fetches resource several times until an expected condition is reached, timeouts, or throws an exception.
    """
    if options.stop is None:
        raise ValueError("options.stop is required")

    for delay in _delayed_loop(options):
        time.sleep(delay)

        resource = fetcher(**args)

        if options.stop(resource):
            return resource

    raise TimeoutError("Timeout while waiting for resource")
