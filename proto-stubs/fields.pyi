from typing import (
    Any,
    Generic,
    Literal,
    MutableMapping,
    MutableSequence,
    NoReturn,
    TypeVar,
    overload,
)

from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper as ProtobufEnum
from google.protobuf.message import Message as ProtobufMessage
from google.protobuf.timestamp_pb2 import Timestamp

from proto.datetime_helpers import DatetimeWithNanoseconds
from proto.enums import Enum
from proto.message import Message
from proto.primitives import ProtoType

_T = TypeVar(
    "_T",
    bound=(
        float
        | int
        | bool
        | str
        | bytes
        | Message
        | Enum
        | ProtobufMessage
        | ProtobufEnum
        | DatetimeWithNanoseconds
    ),
)

_IntegerProtoType = Literal[
    ProtoType.INT64,
    ProtoType.UINT64,
    ProtoType.INT32,
    ProtoType.FIXED64,
    ProtoType.FIXED32,
    ProtoType.UINT32,
    ProtoType.SFIXED32,
    ProtoType.SFIXED64,
    ProtoType.SINT32,
    ProtoType.SINT64,
]

class Field(Generic[_T]):
    repeated: bool
    mcls_data: Any
    parent: Any
    number: int
    proto_type: ProtoType
    message: Any
    enum: Any
    json_name: str | None
    optional: bool
    oneof: str | None

    @overload
    def __init__(
        self: Field[float],
        proto_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[int],
        proto_type: _IntegerProtoType,
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[bool],
        proto_type: Literal[ProtoType.BOOL],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[str],
        proto_type: Literal[ProtoType.STRING],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[bytes],
        proto_type: Literal[ProtoType.BYTES],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # Timestamp is special-cased by proto-plus.
    @overload
    def __init__(
        self: Field[DatetimeWithNanoseconds],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[Timestamp],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # The next overload accepts some non-message types as the message argument,
    # so this overload is needed to forbid that.
    @overload
    def __init__(
        self: Field[NoReturn],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[float | int | bool | str | bytes | Enum | ProtobufEnum],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[_T],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[_T],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # The next overload accepts some non-enum types as the message argument,
    # so this overload is needed to forbid that. Note that we can't forbid
    # int and float because Enum inherits from IntEnum and would match those.
    @overload
    def __init__(
        self: Field[NoReturn],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[bool | str | bytes | Message | ProtobufMessage],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[_T],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[_T],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # Timestamp is special-cased by proto-plus.
    @overload
    def __init__(
        self: Field[DatetimeWithNanoseconds],
        proto_type: type[Timestamp],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # The next overload accepts some non-enum and non-message types,
    # so this overload is needed to forbid that. Note that we can't forbid
    # int and float because Enum inherits from IntEnum and would match those.
    @overload
    def __init__(
        self: Field[NoReturn],
        proto_type: type[bool | str | bytes],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[_T],
        proto_type: type[_T],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: Field[Any],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: Field[Any],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: Field[Any],
        proto_type: str,
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @property
    def descriptor(self): ...
    @property
    def name(self) -> str: ...
    @property
    def package(self) -> str: ...
    @property
    def pb_type(self): ...
    def __get__(self, obj: Message, objtype: type[Message]) -> _T: ...

class RepeatedField(Field[_T]):
    repeated: bool

    @overload
    def __init__(
        self: RepeatedField[float],
        proto_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[int],
        proto_type: _IntegerProtoType,
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[bool],
        proto_type: Literal[ProtoType.BOOL],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[str],
        proto_type: Literal[ProtoType.STRING],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[bytes],
        proto_type: Literal[ProtoType.BYTES],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # Timestamp is special-cased by proto-plus.
    @overload
    def __init__(
        self: RepeatedField[DatetimeWithNanoseconds],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[Timestamp],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # The next overload accepts some non-message types as the message argument,
    # so this overload is needed to forbid that.
    @overload
    def __init__(
        self: RepeatedField[NoReturn],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[float | int | bool | str | bytes | Enum | ProtobufEnum],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[_T],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[_T],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # The next overload accepts some non-enum types as the message argument,
    # so this overload is needed to forbid that. Note that we can't forbid
    # int and float because Enum inherits from IntEnum and would match those.
    @overload
    def __init__(
        self: RepeatedField[NoReturn],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[bool | str | bytes | Message | ProtobufMessage],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[_T],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[_T],
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # Timestamp is special-cased by proto-plus.
    @overload
    def __init__(
        self: RepeatedField[DatetimeWithNanoseconds],
        proto_type: type[Timestamp],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # The next overload accepts some non-enum and non-message types,
    # so this overload is needed to forbid that. Note that we can't forbid
    # int and float because Enum inherits from IntEnum and would match those.
    @overload
    def __init__(
        self: RepeatedField[NoReturn],
        proto_type: type[bool | str | bytes],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[_T],
        proto_type: type[_T],
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: RepeatedField[Any],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: RepeatedField[Any],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: RepeatedField[Any],
        proto_type: str,
        *,
        number: int,
        oneof: str | None = None,
        json_name: str | None = None,
        optional: bool = False,
    ) -> None: ...
    def __get__(self, obj: Message, objtype: type[Message]) -> MutableSequence[_T]: ...  # type: ignore[override]

_K = TypeVar("_K", bound=int | str)
_V = TypeVar(
    "_V",
    bound=(
        float
        | int
        | bool
        | str
        | bytes
        | Message
        | Enum
        | ProtobufMessage
        | ProtobufEnum
        | DatetimeWithNanoseconds
    ),
)

class MapField(Field[_V], Generic[_K, _V]):
    map_key_type: _K
    @overload
    def __init__(
        self: MapField[int, float],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, int],
        key_type: _IntegerProtoType,
        value_type: _IntegerProtoType,
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, bool],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.BOOL],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, str],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.STRING],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, bytes],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.BYTES],
        *,
        number: int,
    ) -> None: ...
    # Timestamp is special-cased by proto-plus.
    @overload
    def __init__(
        self: MapField[int, DatetimeWithNanoseconds],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[Timestamp],
    ) -> None: ...
    # The next overload accepts some non-message types as the message argument,
    # so this overload is needed to forbid that.
    @overload
    def __init__(
        self: MapField[int, NoReturn],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[float | int | bool | str | bytes | Enum | ProtobufEnum],
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, _V],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[_V],
    ) -> None: ...
    # The next overload accepts some non-enum types as the message argument,
    # so this overload is needed to forbid that. Note that we can't forbid
    # int and float because Enum inherits from IntEnum and would match those.
    @overload
    def __init__(
        self: MapField[int, NoReturn],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[bool | str | bytes | Message | ProtobufMessage],
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, _V],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[_V],
    ) -> None: ...
    # Timestamp is special-cased by proto-plus.
    @overload
    def __init__(
        self: MapField[int, DatetimeWithNanoseconds],
        key_type: _IntegerProtoType,
        value_type: type[Timestamp],
        *,
        number: int,
    ) -> None: ...
    # The next overload accepts some non-enum and non-message types,
    # so this overload is needed to forbid that. Note that we can't forbid
    # int and float because Enum inherits from IntEnum and would match those.
    @overload
    def __init__(
        self: MapField[int, NoReturn],
        key_type: _IntegerProtoType,
        value_type: type[bool | str | bytes],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, _V],
        key_type: _IntegerProtoType,
        value_type: type[_V],
        *,
        number: int,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: MapField[int, Any],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: MapField[int, Any],
        key_type: _IntegerProtoType,
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: MapField[int, Any],
        key_type: _IntegerProtoType,
        value_type: str,
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, float],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, int],
        key_type: Literal[ProtoType.STRING],
        value_type: _IntegerProtoType,
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, bool],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.BOOL],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, str],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.STRING],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, bytes],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.BYTES],
        *,
        number: int,
    ) -> None: ...
    # Timestamp is special-cased by proto-plus.
    @overload
    def __init__(
        self: MapField[str, DatetimeWithNanoseconds],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[Timestamp],
    ) -> None: ...
    # The next overload accepts some non-message types as the message argument,
    # so this overload is needed to forbid that.
    @overload
    def __init__(
        self: MapField[str, NoReturn],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[float | int | bool | str | bytes | Enum | ProtobufEnum],
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, _V],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[_V],
    ) -> None: ...
    # The next overload accepts some non-enum types as the message argument,
    # so this overload is needed to forbid that. Note that we can't forbid
    # int and float because Enum inherits from IntEnum and would match those.
    @overload
    def __init__(
        self: MapField[str, NoReturn],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[bool | str | bytes | Message | ProtobufMessage],
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, _V],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[_V],
    ) -> None: ...
    # Timestamp is special-cased by proto-plus.
    @overload
    def __init__(
        self: MapField[str, DatetimeWithNanoseconds],
        key_type: Literal[ProtoType.STRING],
        value_type: type[Timestamp],
        *,
        number: int,
    ) -> None: ...
    # The next overload accepts some non-enum and non-message types,
    # so this overload is needed to forbid that. Note that we can't forbid
    # int and float because Enum inherits from IntEnum and would match those.
    @overload
    def __init__(
        self: MapField[str, NoReturn],
        key_type: Literal[ProtoType.STRING],
        value_type: type[bool | str | bytes],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, _V],
        key_type: Literal[ProtoType.STRING],
        value_type: type[_V],
        *,
        number: int,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: MapField[str, Any],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: MapField[str, Any],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
    ) -> None: ...
    # We can't determine the type when it's passed as a string.
    @overload
    def __init__(
        self: MapField[str, Any],
        key_type: Literal[ProtoType.STRING],
        value_type: str,
        *,
        number: int,
    ) -> None: ...
    def __get__(self, obj: Message, objtype: type[Message]) -> MutableMapping[_K, _V]: ...  # type: ignore[override]
