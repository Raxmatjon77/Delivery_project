from django.shortcuts import render,redirect
from .models import Restaurants
from django.views import View
from .form import RestaurantaCreateForm
# Create your views here.



class RestaurantCreateView(View):
    def get(self,request):
        
        create_form=RestaurantaCreateForm()
        return render(request,'restaurants/add_restaurants.html',{'form':create_form})
    
    def post(self,request):
        
        create_form=RestaurantaCreateForm(request.POST)
        
        
        
        
        if create_form.is_valid():
            
            create_form.save()
            return redirect('landing')
        
        else:
             return render(request,'restaurants/add_restaurants.html',{'form':create_form})
             