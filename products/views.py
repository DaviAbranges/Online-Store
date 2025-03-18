from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .services import ProductService
from .ProductRepository import ProductRepository
from rest_framework import status

class ProductAPIView(APIView):
    def __init__(self, **kwargs):
        self.product_service = ProductService(ProductRepository())

    def get(self, request, product_id=None):

        if product_id:
            product = self.product_service.get_product_by_id(product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            products = self.product_service.get_all_products()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    def post(self, request):
       serializer = ProductSerializer(data=request.data)
       if serializer.is_valid():
           product = self.product_service.create_product(serializer.validated_data)
           return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
       else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id=None):
        product = self.product_service.get_product_by_id(product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            update_product = self.product_service.update_product(product_id, serializer.validated_data)
            return Response(ProductSerializer(update_product).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id=None):
        self.product_service.delete_product(product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
