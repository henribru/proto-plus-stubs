class MessageRule:
    def __init__(self, descriptor: type, wrapper: type) -> None: ...
    def to_python(self, value, *, absent: bool = ...): ...
    def to_proto(self, value): ...
    @property
    def is_map(self): ...
