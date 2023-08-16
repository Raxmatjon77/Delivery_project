from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreateForm
from django.shortcuts import render, redirect
from django.views import View
from .models import User

# Create your views here.

class UserRegisterView(View):
  def get(self,request):

        create_user=UserCreateForm()
        context={
            'form':create_user
        }

        return render(request,'users/register.html',context)
    
  def post(self,request):
        create_form=UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('login')

        else:
            context = {
                'form': create_form
            }

            return render(request, 'users/register.html', context)
class LoginUserView(View):
    def get(self,request):
        login_form=AuthenticationForm()
        context={
            'login_form':login_form
        }
        return render(request,'users/login.html',context)

    def post(self,request):



        login_form=AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user=login_form.get_user()
            login(request, user)
            messages.success(request,'you have successfully logged in !')
            return redirect('landing')

        else:
            return render(request, 'users/login.html', {'login_form':login_form})

