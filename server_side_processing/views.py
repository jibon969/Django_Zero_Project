from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.db.models import Q



def student_data(request):
    """
    This function based view work for Server Side Processing datatable
    :param request:
    :return:
    """
    # Get the data from request
    search_value = request.GET['search[value]'].strip()
    start_length = int(request.GET['start'])
    end_length = start_length + int(request.GET['length'])
    data_array = []

    # Count the total length
    total_student = Student.objects.count()

    # if search parameter is passed
    if search_value != '':
        # Querying dataset
        queryset = Student.objects.filter(
            Q(name__icontains=search_value) |
            Q(roll__icontains=search_value) |
            Q(department__icontains=search_value)
        ).order_by('id')

        # Filtering dataset
        data_filter = queryset[start_length:end_length]

        # Get the filter length
        filter_length = queryset.count()
    else:
        # Querying dataset
        data_list = Student.objects.all().order_by('id')

        # Filtering dataset
        data_filter = data_list[start_length:end_length]

        # Get the filter length
        filter_length = total_student

    # Processing the data for table
    for key, item in enumerate(data_filter):
        row_array = [str(key + 1),
                     item.name,
                     item.department,
                     item.roll,
                     # Foreign key values
                     item.teacher.name,
                     item.created_at
                     ]
        data_array.append(row_array)

    # Preparing the response
    response = {
        "draw": request.GET['draw'],
        "recordsTotal": total_student,
        "recordsFiltered": filter_length,
        "data": data_array
    }

    # Returning json response
    return JsonResponse(response)

