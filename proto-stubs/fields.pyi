from typing import Any, Generic, Literal, TypeVar, overload

from .primitives import ProtoType

T = TypeVar("T")

class Field(Generic[T]):
    repeated: bool
    mcls_data: Any
    parent: Any
    number: Any
    proto_type: ProtoType
    message: Any
    enum: Any
    json_name: Any
    optional: Any
    oneof: Any
    @overload
    def __init__(
        self: Field[float],
        proto_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[int],
        proto_type: Literal[
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
        ],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[bool],
        proto_type: Literal[ProtoType.BOOL],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[str],
        proto_type: Literal[ProtoType.STRING],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[bytes],
        proto_type: Literal[ProtoType.BYTES],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[T],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[T],
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[T],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[T],
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[T],
        proto_type: type[T],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[Any],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Field[Any],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @property
    def descriptor(self): ...
    @property
    def name(self) -> str: ...
    @property
    def package(self) -> str: ...
    @property
    def pb_type(self): ...
    def __get__(self, obj, objtype=None) -> T: ...

class RepeatedField(Field[T]):
    repeated: bool
    @overload
    def __init__(
        self: RepeatedField[float],
        proto_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[int],
        proto_type: Literal[
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
        ],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[bool],
        proto_type: Literal[ProtoType.BOOL],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[str],
        proto_type: Literal[ProtoType.STRING],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[bytes],
        proto_type: Literal[ProtoType.BYTES],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[T],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[T],
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[T],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[T],
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[T],
        proto_type: type[T],
        *,
        number: int,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[Any],
        proto_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: RepeatedField[Any],
        proto_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
        oneof: str = ...,
        json_name: str = ...,
        optional: bool = ...,
    ) -> None: ...
    def __get__(self, obj, objtype=None) -> list[T]: ...  # type: ignore[override]

K = TypeVar("K")
V = TypeVar("V")

class MapField(Field[V], Generic[K, V]):
    map_key_type: K
    @overload
    def __init__(
        self: MapField[int, float],
        key_type: Literal[
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
        ],
        value_type: Literal[ProtoType.DOUBLE, ProtoType.FLOAT],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, int],
        key_type: Literal[
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
        ],
        value_type: Literal[
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
        ],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, bool],
        key_type: Literal[
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
        ],
        value_type: Literal[ProtoType.BOOL],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, str],
        key_type: Literal[
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
        ],
        value_type: Literal[ProtoType.STRING],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, bytes],
        key_type: Literal[
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
        ],
        value_type: Literal[ProtoType.BYTES],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, V],
        key_type: Literal[
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
        ],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[V],
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, V],
        key_type: Literal[
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
        ],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[V],
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, V],
        key_type: Literal[
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
        ],
        value_type: type[V],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, Any],
        key_type: Literal[
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
        ],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[int, Any],
        key_type: Literal[
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
        ],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
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
        value_type: Literal[
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
        ],
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
    @overload
    def __init__(
        self: MapField[str, V],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: type[V],
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, V],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: type[V],
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, V],
        key_type: Literal[ProtoType.STRING],
        value_type: type[V],
        *,
        number: int,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, Any],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.MESSAGE],
        *,
        number: int,
        message: str,
    ) -> None: ...
    @overload
    def __init__(
        self: MapField[str, Any],
        key_type: Literal[ProtoType.STRING],
        value_type: Literal[ProtoType.ENUM],
        *,
        number: int,
        enum: str,
    ) -> None: ...
    def __get__(self, obj, objtype=None) -> dict[K, V]: ...  # type: ignore[override]
