from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=120)
    teacherID = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teacher'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=120)
    roll = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name
