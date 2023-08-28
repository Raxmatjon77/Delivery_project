from django.contrib import admin
from .models import Delivery, DeliverySet


class DeliverySetInline(admin.TabularInline):
    model = DeliverySet
    extra = 1
    

class DeliveryProductAdmin(admin.ModelAdmin):
    inlines = [DeliverySetInline]

admin.site.register(Delivery, DeliveryProductAdmin)