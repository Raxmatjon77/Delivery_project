from django.db import models
# from products.models import Product
from django.contrib.auth.models import AbstractUser


NEW, CODE_VERIFIED, DONE = ('new', 'code_verified', 'done')

class User(AbstractUser):
    class ADDRESS(models.TextChoices):        
        TASHKENT = ("Toshkent", "toshkent")
        NAMANGAN = ("Namangan", "namangan")
        FERGANA = ("Fa'gona", "farg'ona")
        BUKHARA = ("Buxoro", "buxoro")
        NAVAIY = ("Navoiy", "navoiy")
        SYRDARYA = ("sirdaryo", "sirdaryo")
        SAMARKAND = ("Samarqand, samarqand")
        KARAKALPAKSTAN = ("Qoraqalpog'iston", "qoraqalpog'iston")
        JIZZAKH = ("Jizzah", "jizzah")
        SURKHANDARYA = ("Surxondaryo", "surxondaryo")
        KASHKADARYA = ("Qashqadaryo", "qashqadaryo")

    AUTH_STATUS = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
        (DONE, DONE),
        
    )
    profile_picture=models.ImageField(upload_to="profile_pictures", default='default_profile_pic.jpg',blank=True) 
    auth_status=models.CharField(max_length=35, choices=AUTH_STATUS,default=NEW)
    region = models.CharField(max_length=35, choices=ADDRESS.choices,default=ADDRESS.TASHKENT)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    
    
# class Orders(models.Model):
#     name=models.ForeignKey(Product,related_name='product',on_delete=models.CASCADE)
#     quantity=models.IntegerField()
    

