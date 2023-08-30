from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List
from dateutil import parser


@dataclass
class TimeSeriesPoint:
    """
    Represents a point in a TimeSeries.
    """

    timestamp: datetime
    """
    Date of the point.
    """

    value: float
    """
    Value of the point.
    """


def unmarshal_TimeSeriesPoint(data: Any) -> TimeSeriesPoint:
    """
    Unmarshal an instance of TimeSeriesPoint from the given data.
    """
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TimeSeriesPoint' failed as data isn't a dictionary."
        )

    return TimeSeriesPoint(
        timestamp=parser.isoparse(data["timestamp"]),
        value=data["value"],
    )


def marshal_TimeSeriesPoint(data: TimeSeriesPoint) -> Dict[str, Any]:
    """
    Marshal an instance of TimeSeriesPoint into a JSON compatible data structure.
    """
    return {
        "timestamp": data.timestamp.isoformat(),
        "value": data.value,
    }


@dataclass
class TimeSeries:
    """
    Represents a time series that could be used for graph purposes.
    """

    name: str
    """
    Name of the metric.
    """

    points: List[TimeSeriesPoint]
    """
    Points contains all the points that composed the series.
    """

    metadata: Dict[str, str]
    """
    Metadata contains some string metadata related to a metric.
    """


def unmarshal_TimeSeries(data: Any) -> TimeSeries:
    """
    Unmarshal an instance of TimeSeries from the given data.
    """
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'TimeSeries' failed as data isn't a dictionary."
        )

    return TimeSeries(
        name=data["name"],
        points=[unmarshal_TimeSeriesPoint(point) for point in data["points"]],
        metadata=data["metadata"],
    )


def marshal_TimeSeries(data: TimeSeries) -> Dict[str, Any]:
    """
    Marshal an instance of TimeSeries into a JSON compatible data structure.
    """
    return {
        "name": data.name,
        "points": [marshal_TimeSeriesPoint(point) for point in data.points],
        "metadata": data.metadata,
    }
