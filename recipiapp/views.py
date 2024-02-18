from django.shortcuts import render, redirect
from .models import Recipies
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def recipipage(request):
  
    if request.method == 'POST':
        data = request.POST
        recipiName = data.get('recipi_name')
        recipiDes = data.get('recipi_description')
        recipiImg = request.FILES.get('recipi_image')
        Recipies.objects.create(recipi_name = recipiName,recipi_description = recipiDes, recipi_image = recipiImg)
        return redirect('recipi')

    queryset = Recipies.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipi_name__icontains = request.GET.get('search'))
    return render(request, 'recipi.html',{'title':'Recipi Page','recipies':queryset})

@login_required(login_url='login')
def delete_recipi(request,id):
    queryset = Recipies.objects.get(id = id)
    queryset.delete()
    return redirect('recipi')

@login_required(login_url='login')
def update_recipi(request, id):
    queryset = Recipies.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        recipiName = data.get('recipi_name')
        recipiDes = data.get('recipi_description')
        recipiImg = request.FILES.get('recipi_image')
        queryset.recipi_name = recipiName
        queryset.recipi_description = recipiDes
        if recipiImg:
            queryset.recipi_image = recipiImg
        queryset.save()
        return redirect('recipi')

    return render(request, 'updaterecipi.html',{'title':'Update Page','recipi':queryset})

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        firstName = data.get('first_name')
        lastName = data.get('last_name')
        username = data.get('user_name')
        password = data.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request,'Username already taken')
            return redirect('register')

        user = User.objects.create(first_name = firstName, last_name = lastName, username = username)
        user.set_password(password)
        user.save()
        messages.success(request, 'Registered Successfully')
        # print(User.objects.all())
        return redirect('register')

    return render(request, 'register.html', {'title':'Register Page'})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request,'User does not exists')
            return redirect('login')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('recipi')

    return render(request, 'login.html',{'title':'Login Page'})

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')