from django.urls import path
from csv_file.views import (
    product_list,
    download_product_csv,
    product_download_by_date_csv

)

urlpatterns = [
    path('product-list/', product_list, name="product-list"),
    path('download-product-csv/', download_product_csv, name="download-product-csv"),
    path('product-download-by-date-csv/', product_download_by_date_csv, name="product-download-by-date-csv"),
]
