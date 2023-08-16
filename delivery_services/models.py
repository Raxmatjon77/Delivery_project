from django.db import models
from products.models import Product
from users.models import User
from restaurants.models import Restaurants
# Create your models here.
class DeliveryService(models.Model):
    name=models.CharField(max_length=100, unique=True)
    about_service=models.TextField()
    service_logo=models.ImageField(upload_to='service_logo',default='default_service_logo.jpg',blank=True)
    
    
    
    def __str__(self):
        return f"{self.name}"
    
# Create your models here.
class Delivery(models.Model):
    class IS_DELIVERED(models.TextChoices):
        PENDING=('Pending','pending'),
        IN_TRANSIT=('In transit','in Transit'),
        IS_DELIVERED=('Is Delivered','is delivered')
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    delivery_address = models.CharField(max_length=100)
    delivery_date = models.DateField()
   
    total_price = models.IntegerField()
    is_delivered = models.CharField(choices=IS_DELIVERED.choices,default=IS_DELIVERED.PENDING,max_length=50)
    
    def __str__(self):
        return f"{self.products.all() }  from {self.restaurant} to {self.user} , {self.delivery_address}"
