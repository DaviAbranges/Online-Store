

from django.urls import path

path('products/', ProductList.as_view(), name='product-list'),