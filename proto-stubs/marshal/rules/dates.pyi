from datetime import timedelta, timezone as timezone

from google.protobuf import duration_pb2, timestamp_pb2

from proto import datetime_helpers as datetime_helpers, utils as utils

class TimestampRule:
    def to_python(
        self, value, *, absent: bool | None = None
    ) -> datetime_helpers.DatetimeWithNanoseconds: ...
    def to_proto(self, value) -> timestamp_pb2.Timestamp: ...

class DurationRule:
    def to_python(self, value, *, absent: bool | None = None) -> timedelta: ...
    def to_proto(self, value) -> duration_pb2.Duration: ...
