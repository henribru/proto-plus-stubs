from collections.abc import Mapping
from typing import Any, Literal, TypeVar, overload

from google.protobuf import descriptor_pb2, message

from proto.fields import Field
from proto.marshal import Marshal

_M = TypeVar("_M")

class MessageMeta(type):
    def __new__(mcls, name, bases, attrs): ...
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs): ...
    @property
    def meta(cls): ...
    @overload
    def pb(
        cls: type[_M], obj: None = None, *, coerce: bool = False
    ) -> type[message.Message]: ...
    @overload
    def pb(
        cls: type[_M], obj: _M, *, coerce: Literal[False] = False
    ) -> message.Message: ...
    @overload
    def pb(
        cls: type[_M], obj: _M | Mapping | message.Message, *, coerce: Literal[True]
    ) -> message.Message: ...
    def wrap(cls: type[_M], pb: message.Message) -> _M: ...
    def serialize(cls: type[_M], instance: _M | Mapping | message.Message) -> bytes: ...
    def deserialize(cls: type[_M], payload: bytes) -> _M: ...
    def to_json(
        cls: type[_M],
        instance: _M,
        *,
        use_integers_for_enums: bool = True,
        including_default_value_fields: bool = True,
        preserving_proto_field_name: bool = False,
        sort_keys: bool = False,
        indent: int | None = 2,
        float_precision: int | None = None,
    ) -> str: ...
    def from_json(
        cls: type[_M], payload: str, *, ignore_unknown_fields: bool = False
    ) -> _M: ...
    def to_dict(
        cls: type[_M],
        instance: _M,
        *,
        use_integers_for_enums: bool = True,
        preserving_proto_field_name: bool = True,
        including_default_value_fields: bool = True,
        float_precision: int | None = None,
    ) -> dict[str, Any]: ...
    def copy_from(
        cls: type[_M], instance: _M, other: _M | Mapping | message.Message
    ) -> None: ...

class Message(metaclass=MessageMeta):
    _pb: message.Message

    def __init__(
        self: _M,
        mapping: _M | Mapping | message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        **kwargs,
    ) -> None: ...
    def __contains__(self, key: str) -> bool: ...

class _MessageInfo:
    package: Any
    full_name: Any
    options: Any
    fields: Any
    fields_by_number: Any
    marshal: Any
    def __init__(
        self,
        fields: list[Field],
        package: str,
        full_name: str,
        marshal: Marshal,
        options: descriptor_pb2.MessageOptions,
    ) -> None: ...
    @property
    def pb(self) -> type[message.Message]: ...
