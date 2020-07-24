from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from calories.models import Consume
import datetime
from dateutil.parser import parse

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username}, your account has been created.')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request,'users/register.html',{'form':form})

@login_required
def profilepage(request):
    consumed_food = Consume.objects.filter(user=request.user)
    consumed_food_date = Consume.objects.filter(user=request.user)
    if request.method == "POST":
        date = parse(request.POST['date_consumed'])        
        date_consume = date.strftime('%Y-%m-%d')
        user = request.user
        consumed_food = consumed_food.filter(date=date_consume)
    else:
        consumed_food = Consume.objects.filter(user=request.user)
    
    return render(request,'users/profile.html',{'consumed_food':consumed_food, 'consumed_food_date':consumed_food_date})