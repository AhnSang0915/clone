from typing import Any

class Descriptor:
    name: Any
    def __init__(self, name: Any | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Typed(Descriptor):
    expected_type: Any
    allow_none: bool
    nested: bool
    __doc__: Any
    def __init__(self, *args, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Convertible(Typed):
    def __set__(self, instance, value) -> None: ...

class Max(Convertible):
    expected_type: Any
    allow_none: bool
    def __init__(self, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Min(Convertible):
    expected_type: Any
    allow_none: bool
    def __init__(self, **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class MinMax(Min, Max): ...

class Set(Descriptor):
    __doc__: Any
    def __init__(self, name: Any | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class NoneSet(Set):
    def __init__(self, name: Any | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Integer(Convertible):
    expected_type: Any

class Float(Convertible):
    expected_type: Any

class Bool(Convertible):
    expected_type: Any
    def __set__(self, instance, value) -> None: ...

class String(Typed):
    expected_type: Any

class Text(String, Convertible): ...

class ASCII(Typed):
    expected_type: Any

class Tuple(Typed):
    expected_type: Any

class Length(Descriptor):
    def __init__(self, name: Any | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class Default(Typed):
    def __init__(self, name: Any | None = ..., **kw) -> None: ...
    def __call__(self): ...

class Alias(Descriptor):
    alias: Any
    def __init__(self, alias) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...

class MatchPattern(Descriptor):
    allow_none: bool
    test_pattern: Any
    def __init__(self, name: Any | None = ..., **kw) -> None: ...
    def __set__(self, instance, value) -> None: ...

class DateTime(Typed):
    expected_type: Any
    def __set__(self, instance, value) -> None: ...
