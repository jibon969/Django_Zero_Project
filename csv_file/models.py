from django.db import models
from django.db.models import Q, QuerySet
from django.db.models.signals import pre_save
from django_zero_project.utils import unique_slug_generator


class Brand(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
    image = models.FileField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


def brand_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(brand_pre_save_receiver, sender=Brand)


class ProductManagerQueryset(models.query.QuerySet):
    """
    ProductInventory model queryset
    """
    def by_range(self,  start_date, end_date=None):
        if end_date is None:
            return self.filter(update__gte=start_date)
        return self.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)


class ProductManager(models.Manager):
    """
    This model manager work download product_inventory by date
    """
    def get_queryset(self):
        return ProductManagerQueryset(self.model, using=self._db)

    def product_by_date(self, start_date, end_date):
        return self.get_queryset().by_range(start_date, end_date)


class Product(models.Model):
    title = models.CharField(max_length=120)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=450)
    old_price = models.DecimalField(default=1000, max_digits=20, decimal_places=2)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']

