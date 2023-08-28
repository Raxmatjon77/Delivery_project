from django.db import models

from delivery_services.models import Delivery


class Product(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField()
    price=models.IntegerField()
    delivery=models.ForeignKey(Delivery, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productimage')
    image = models.ImageField(upload_to='products_pictures')
