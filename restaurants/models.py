from django.db import models
from products.models import Product



class Restaurants(models.Model):
    name=models.CharField(max_length=60, unique=True)
    image = models.ImageField(upload_to="restaurants_logos")
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='offers')
    location=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    

