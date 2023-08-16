from django.shortcuts import render,redirect
from .models import Product,ProductImage
from django.views import View
from .forns import ProductCreateForm
# Create your views here.

class ProductCreateView(View):
    def get(self,request):
        
        create_form=ProductCreateForm()
        return render(request,'products/add_product.html',{'form':create_form})
    
    def post(self,request):
        
        create_form=ProductCreateForm(request.POST)
        
        
        
        
        if create_form.is_valid():
            
            create_form.save()
            return redirect('landing')
        
        else:
             return render(request,'products/add_product.html',{'form':create_form})
            
            
            
        