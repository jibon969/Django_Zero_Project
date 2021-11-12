from django.urls import path
from csv_file.views import (
    product_list
)

urlpatterns = [
    path('product-list/', product_list, name="product-list"),
]