from django.urls import path
from .views import RestaurantCreateView

urlpatterns = [
    path('add/',RestaurantCreateView.as_view(),name='add_restaurant')
]
