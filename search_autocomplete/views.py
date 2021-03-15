from django.shortcuts import render
from .models import Language


def search_autocomplete(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, "search_autocomplete/search_autocomplete.html", context)