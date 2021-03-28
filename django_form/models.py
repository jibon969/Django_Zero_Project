from django.db import models


class Course(models.Model):
    subject = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-timestamp']


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=120)
    subject_name = models.ManyToManyField(Course)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher_name

    class Meta:
        ordering = ['-timestamp']
