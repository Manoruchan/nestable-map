from typing import Any
from NestableMap import NestableMap


map = NestableMap[str, Any]()

map.set("a", { "b": 0 })
map.set("a.b", 1)

# 0 if deep access is true
# 1 if deep access is false
print(map.get("a.b"))

# do nothing if not overridable
map.set("a", 2)
print(map.get("a"))


@map.forEach
def log(v: str, k: Any):
    print(f"{k}: {v}")

def l(v: str, k: Any):
    print(f"{k}: {v}")

map.forEach(l)

map.forEach(lambda v, k: print(f"{k}: {v}"))
