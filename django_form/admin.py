from django.contrib import admin
from .models import Course, Teacher


class CourseAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['subject', 'timestamp', 'update']

    class Meta:
        model = Course


admin.site.register(Course, CourseAdmin)

admin.site.register(Teacher)