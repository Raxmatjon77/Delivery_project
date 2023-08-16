from django.urls import path
from .views import ProductCreateView
urlpatterns = [
    path('add/',ProductCreateView.as_view(),name='add_product')
]
