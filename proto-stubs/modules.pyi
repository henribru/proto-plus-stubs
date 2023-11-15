from typing import Any, NamedTuple

class _ProtoModule(NamedTuple):
    package: Any
    marshal: Any
    manifest: Any

def define_module(
    package: str, *, marshal: str | None = None, manifest: set[str] = ...
) -> _ProtoModule: ...
