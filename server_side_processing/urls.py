from django.urls import path
from . import views

urlpatterns = [
    path('student-data/', views.student_data, name='student-data'),
]

