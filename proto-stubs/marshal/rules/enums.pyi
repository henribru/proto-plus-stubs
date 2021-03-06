import enum
from typing import Type

class EnumRule:
    def __init__(self, enum_class: Type[enum.IntEnum]) -> None: ...
    def to_python(self, value, *, absent: bool = ...): ...
    def to_proto(self, value): ...
