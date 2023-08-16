from django.urls import path
from .views import UserRegisterView,LoginUserView
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
    path('login/',LoginUserView.as_view(), name='login')
]
