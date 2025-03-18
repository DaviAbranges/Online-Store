from .ProductRepository import ProductRepository
from typing import List
from .models import Product
class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def get_all_products(self) -> List[Product]:
        return self.product_repo.get_all_products()

    def get_product_by_id(self, product_id: int) -> Product:
        return self.product_repo.get_product_by_id(product_id)

    def create_product(self, product: Product) -> Product:
        return self.product_repo.create_product(product)

    def update_product(self, product_id: int, product: Product) -> Product:
        return self.product_repo.update_product(product_id, product)

    def delete_product(self, product_id: int) -> None:
        return self.product_repo.delete_product(product_id)