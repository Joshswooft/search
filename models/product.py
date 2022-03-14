from dataclasses import dataclass
from typing import Any

from utils import from_int, from_str


@dataclass
class Product:
    id: int
    name: str
    brand: str

    @staticmethod
    def from_dict(obj: Any) -> 'Product':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        brand = from_str(obj.get("brand"))
        return Product(id, name, brand)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["brand"] = from_str(self.brand)
        return result

