from django.urls import path
from .views import ProductAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='product-list'),\
    path('products/<int:product_id>/', ProductAPIView.as_view(), name='product-detail')
]
