from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.TextField(null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, null=False, blank=False)
    code = models.CharField(
        max_length=10, null=False, blank=False)
    description = models.TextField()
    category = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name
