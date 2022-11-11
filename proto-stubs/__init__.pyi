from typing import Any, Literal

from .enums import Enum as Enum
from .fields import Field as Field, MapField as MapField, RepeatedField as RepeatedField
from .marshal import Marshal as Marshal
from .message import Message as Message
from .modules import define_module as module
from .primitives import ProtoType

DOUBLE: Literal[ProtoType.DOUBLE]
FLOAT: Literal[ProtoType.FLOAT]
INT64: Literal[ProtoType.INT64]
UINT64: Literal[ProtoType.UINT64]
INT32: Literal[ProtoType.INT32]
FIXED64: Literal[ProtoType.FIXED64]
FIXED32: Literal[ProtoType.FIXED32]
BOOL: Literal[ProtoType.BOOL]
STRING: Literal[ProtoType.STRING]
MESSAGE: Literal[ProtoType.MESSAGE]
BYTES: Literal[ProtoType.BYTES]
UINT32: Literal[ProtoType.UINT32]
ENUM: Literal[ProtoType.ENUM]
SFIXED32: Literal[ProtoType.SFIXED32]
SFIXED64: Literal[ProtoType.SFIXED64]
SINT32: Literal[ProtoType.SINT32]
SINT64: Literal[ProtoType.SINT64]
