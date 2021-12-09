from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from faker import Faker
fake = Faker()
from . models import *


def generate_data(request):
    for i in range(0, 100):
        FakeAddress.objects.create(address=fake.address())
    return JsonResponse({'status': 200})


def auto_complete_search(request):

    return render(request, "auto_complete_search/auto_complete_search.html")


def search_address(request):
    address = request.GET.get('address')
    payload = []
    if address:
        fake_address_objs = FakeAddress.objects.filter(
            address__icontains=address
        )
        for fake_address_obj in fake_address_objs:
            payload.append(fake_address_obj.address)
    return JsonResponse({'status': 200, 'data': payload})