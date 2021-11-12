from django.contrib import admin
from .models import Brand, Product


class BrandAdmin(admin.ModelAdmin):

    class Meta:
        model = Brand
        list_display = ['title', 'slug', 'image', 'active', 'timestamp']
        search_fields = ['title']


admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
        list_display = ['title', 'brand', 'timestamp']
        search_fields = ['title']


admin.site.register(Product, ProductAdmin)