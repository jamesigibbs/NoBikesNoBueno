from django.db import models

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name