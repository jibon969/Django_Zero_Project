from django.db import models


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True)
    price = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.name}"
