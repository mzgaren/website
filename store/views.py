from django.shortcuts import render, redirect
from .models import Product, Order, Customer, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django import forms
from .forms import SignUpForm

def category(request, foo):
    #replace Hyphens with a spaces
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, "That Category doesn't exist")
        return redirect('home')
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})

def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'products': product})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have Been Logged In')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging In please try again')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have Been logged out")
    return redirect('login')

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form_is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Been registered")
            return redirect('home')
        else:
            messages.success(request, "There was an error, Please try again")
            return redirect('register')

    else:
        return render(request, 'register.html', {'form': form})
