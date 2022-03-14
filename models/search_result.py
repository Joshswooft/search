from dataclasses import dataclass
from typing import Any
from models.product import Product
from utils import from_float, to_class, to_float

@dataclass
class SearchResult:
    score: float
    product: Product
    
    @staticmethod
    def from_dict(obj: Any) -> 'SearchResult':
        assert isinstance(obj, dict)
        score = from_float(obj.get("Score"))
        product = Product.from_dict(obj.get("product"))
        return SearchResult(score, product)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Score"] = to_float(self.score)
        result["product"] = to_class(Product, self.product)
        return result