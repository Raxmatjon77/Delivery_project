from django.db import models
from products.models import Product
from django.contrib.auth.models import AbstractUser
# Create your models here.



NEW, CODE_VERIFIED, DONE = ('new', 'code_verified', 'done')
TASHKENT,NAMANGAN,FERGANA, \
    BUKHARA,NAVAIY,SYRDARYA,SAMARKAND,KARAKALPAKSTAN,\
        JIZZAKH,SURKHANDARYA,\
            KASHKADARYA=('tashkent','namangan','fergana','bukhara','navaiy','syrdarya','samarkand','karakalpakstan','jizzakh','surkhandarya')
class User(AbstractUser):
    AUTH_STATUS = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
        (DONE, DONE),
        
    )
    ADRESSES=((TASHKENT,TASHKENT),
              (NAMANGAN,NAMANGAN),
              (FERGANA,FERGANA),
              (BUKHARA,BUKHARA),
              (NAVAIY,NAVAIY),
              (SYRDARYA,SYRDARYA),
              (SAMARKAND,SAMARKAND),
              (KARAKALPAKSTAN,KARAKALPAKSTAN),
              (JIZZAKH,JIZZAKH),
              (SURKHANDARYA,SURKHANDARYA),
              (KASHKADARYA,KASHKADARYA))
    profile_picture=models.ImageField(default='default_profile_pic.jpg',blank=True) 
    auth_status=models.CharField(choices=AUTH_STATUS,default=NEW)
    region = models.CharField(max_length=35, choices=ADRESSES,default=TASHKENT)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
# class Orders(models.Model):
#     name=models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
#     quantity=models.IntegerField()
    

