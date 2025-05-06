from typing import Generic, TypeVar, Callable, Optional, Self, Any
from collections import OrderedDict
from collections.abc import KeysView, ValuesView, ItemsView

K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("U")

class NestableMap(Generic[K, V]):
    _dict: OrderedDict[K, V]
    _deepAccess: bool
    _overridable: bool
    _delimiter: str

    def __init__(
        self,
        initDict: dict[K, V] = {},
        deepAccess: bool = True,
        overridable: bool = True,
        parseStr: str = "."
    ):
        self._dict = OrderedDict(initDict)
        self._deepAccess = deepAccess
        self._overridable = overridable
        self._delimiter = parseStr

    def _parseKey(self, k: str) -> list[str]:
        return k.split(self._delimiter)

    def _keyTypeValidation(self, k: K):
        if self._deepAccess and not isinstance(k, str):
            raise TypeError("When deepAccess is True, key must be a string")

    def clear(self):
        self._dict.clear()

    def compute(self, k: K, remapper: Callable[[K, Optional[V]], Optional[V]]) -> Optional[V]:
        v = remapper(k, self.get(k, False))
        if v:
            self.set(k, v)
        else:
            self.delete(k)
        return v

    def computeIfAbsent(self, k: K, mapper: Callable[[K], Optional[V]]) -> V:
        v = self.get(k, False)
        if not v:
            v = mapper(k)
            self.set(k, v)
        return v

    def computeIfPresent(self, k: K, remapper: Callable[[K, V], V]) -> Optional[V]:
        currentV = self.get(k, False)
        if currentV:
            v = remapper(k, currentV)
            if v is None:
                self.delete(k)
            else:
                self.set(k, v)
            return v

    def delete(self, k: K):
        del self._dict[k]

    def find(self, fn: Callable[[V, K], bool]) -> Optional[V]:
        for k, v in self._dict.items():
            if fn(v, k):
                return v

    def forEach(self, fn: Callable[[V, K], None] = None):
        if fn == None:
            def deco(f: Callable[[V, K], None]):
                for k, v in self._dict.items():
                    f(v, k)
                return f
            return deco
        else:
            for k, v in self._dict.items():
                fn(v, k)

    def get(self, k: K, deepAccess: bool = True) -> Optional[V]:
        """Search nested dictionaries if deepAccess is enabled."""
        self._keyTypeValidation(k)
        return self.search(self._parseKey(k)) if self._deepAccess and deepAccess else self._dict.get(k)

    def getOrDef(self, k: K, default: V) -> V:
        return self.get(k) or default

    def has(self, k: K) -> bool:
        return k in self._dict or (self._deepAccess and self.search(self._parseKey(k)) is not None)

    def items(self) -> ItemsView[K, V]:
        return self._dict.items()

    def keys(self) -> KeysView[K]:
        return self._dict.keys()

    def search(self, keys: list[str]) -> Optional[T]:
        via: dict = self._dict

        for key in keys[:-1]:
            v: Any = via.get(key)
            if not isinstance(v, dict):
                return None
            via = v

        return via.get(keys[-1]) if keys else None

    def set(self, k: K, v: V) -> Self:
        if self._overridable:
            self._dict[k] = v
        elif k not in self._dict:
            self._dict[k] = v
        return self

    @property
    def size(self) -> int:
        return len(self._dict)

    def values(self) -> ValuesView[V]:
        return self._dict.values()
