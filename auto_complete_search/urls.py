from django.urls import path
from . import views

urlpatterns = [
    path('generate-data/', views.generate_data, name='generate-data'),
    path('auto-complete-search/', views.auto_complete_search, name='auto-complete-search'),
    path('search/', views.search_address, name='search'),

]
