from typing import Any, Awaitable, Callable, Dict, List, Optional, Type, TypeVar

T = TypeVar("T")


def _build_fetcher_args(
    args: Dict[str, Any],
    page: Optional[int],
) -> Dict[str, Any]:
    """
    Builds the arguments to pass to the fetcher function.
    """
    return {
        **args,
        "page": page or args.get("page") or 1,
    }


def fetch_all_pages(
    type: Type[T],
    key: str,
    fetcher: Callable[..., T],
    args: Dict[str, Any],
    page: Optional[int] = None,
) -> List[Any]:
    """
    :param key: The key to use to get the list of items from the response
    :param fetcher: The function to call to fetch the response
    :return: The list of items
    """
    fetcher_args = _build_fetcher_args(args, page)
    page = fetcher_args.get("page") or 1
    page_size = fetcher_args.get("page_size")

    data = fetcher(**fetcher_args)
    if not data:
        return []

    items: List[Any] = getattr(data, key)

    if page_size is not None and len(items) < page_size:
        return items

    if not items:
        return items

    return items + fetch_all_pages(
        type=type,
        key=key,
        fetcher=fetcher,
        args=args,
        page=page + 1,
    )


async def fetch_all_pages_async(
    type: Type[T],
    key: str,
    fetcher: Callable[..., Awaitable[T]],
    args: Dict[str, Any],
    page: Optional[int] = None,
) -> List[Any]:
    """
    :param key: The key to use to get the list of items from the response
    :param fetcher: The function to call to fetch the response
    :return: The list of items
    """
    fetcher_args = _build_fetcher_args(args, page)
    page = fetcher_args.get("page") or 1
    page_size = fetcher_args.get("page_size")

    data = await fetcher(**fetcher_args)
    if not data:
        return []

    items: List[Any] = getattr(data, key)

    if page_size is not None and len(items) < page_size:
        return items

    if not items:
        return items

    return items + await fetch_all_pages_async(
        type=type,
        key=key,
        fetcher=fetcher,
        args=args,
        page=page + 1,
    )
