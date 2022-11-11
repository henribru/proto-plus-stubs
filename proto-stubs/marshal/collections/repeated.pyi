import collections.abc
from typing import Any

from proto.utils import cached_property as cached_property

class Repeated(collections.abc.MutableSequence):
    def __init__(self, sequence, marshal, *, proto_type: Any | None = ...) -> None: ...
    def __copy__(self): ...
    def __delitem__(self, key) -> None: ...
    def __eq__(self, other): ...
    def __getitem__(self, key): ...
    def __len__(self): ...
    def __ne__(self, other): ...
    def __setitem__(self, key, value) -> None: ...
    def insert(self, index: int, value): ...
    def sort(self, *, key: str = ..., reverse: bool = ...): ...
    @property
    def pb(self): ...

class RepeatedComposite(Repeated):
    def __eq__(self, other): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def insert(self, index: int, value): ...