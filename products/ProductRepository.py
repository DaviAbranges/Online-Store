from .models import Product
from typing import List

class ProductRepository:
    def get_all_products(self) -> List[Product]:
        return Product.objects.all()

    def get_product_by_id(self, product_id: int) -> Product:
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None

    def create_product(self, product_data: dict) -> Product:
        product = Product.objects.create(**product_data)
        return product

    def update_product(self, product_id: int, product_data: dict) -> Product:
        product = self.get_product_by_id(product_id)
        if product:
            for key, value in product_data.items():
                setattr(product, key, value)
            product.save()
            return product
        return None

    def delete_product(self, product_id: int) -> bool:
        product = self.get_product_by_id(product_id)
        if product:
            product.delete()
            return True
        return False
