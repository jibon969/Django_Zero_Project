from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
import csv
from django.http import HttpResponse


def product_list(request):
    """
    This function based view work for show all product
    :param request:
    :return:
    """
    posts_list = Product.objects.all()
    query = request.GET.get('q')
    if query:
        # Using strip method to remove extra white space
        query = query.strip()
        posts_list = Product.objects.filter(
            Q(title__icontains=query) |
            Q(title__startswith=query) |
            Q(title__endswith=query)
        ).distinct()
    paginator = Paginator(posts_list, 10)  # 10 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'object_list': posts,
        'page': page
    }

    return render(request, "csv_file/product_csv.html", context)


def download_product_csv(request):
    # queryset = Product.objects.all().values_list('title', 'brand')
    queryset = Product.objects.all()
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow([
       'Title', 'Brand', 'Image', 'Price', 'Old Price'
    ])
    for q in queryset:
        row = []
        row.extend([
            q.title, q.brand.title, q.image, q.price, q.old_price
        ])
        writer.writerow(row[:])
    response['Content-Disposition'] = 'attachment; filename="product.csv"'
    return response
