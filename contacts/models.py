from django.core.validators import RegexValidator
from django.db import models


class Contact(models.Model):
    subject = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(
        regex="^(?:\+88|01)?\d{11}$",
        message="Phone number must be entered in the format: '+88 01734567891'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
