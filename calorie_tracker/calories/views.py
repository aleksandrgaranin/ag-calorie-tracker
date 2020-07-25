from django.shortcuts import render,redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import FoodForm
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



class CreateFood(CreateView):
    model = Food
    fields = ['user', 'name', 'carbs', 'protein', 'fat', 'calories']
    template_name = 'calories/food-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

def update_food(request,id):
    food = Food.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=food)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request, 'calories/food-form.html',{'form':form,'food':food})

def delete_food(request,id):
    food = Food.objects.get(id=id)

    if request.method == 'POST':
        food.delete()
        return redirect('index')

    return render(request,'calories/food-delete.html',{'food':food})

class DetaleClassView(DetailView):
    model = Food
    template_name = 'calories/detail.html'


class FoodView(ListView):
    model = Food
    template_name = 'calories/food-list.html'
    context_object_name = 'item_list'