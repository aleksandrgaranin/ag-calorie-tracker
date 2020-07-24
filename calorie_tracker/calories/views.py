from django.shortcuts import render,redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required
def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        date = datetime.date.today()
        consume = Consume(date=date, user=user, food_concumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:        
        foods = Food.objects.all()
    date = datetime.date.today()
    consumed_food = Consume.objects.filter(user=request.user,date=date)
    
    return render(request,'calories/index.html',{'foods':foods, 'consumed_food':consumed_food})


@login_required
def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/index')
    return render(request,'calories/delete.html')
    

def welcome(request):
    return render(request,'calories/welcome.html')