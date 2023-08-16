from django.views import View
from django.shortcuts import redirect,render
def landing(request):
        
  return render(request,'landing.html')