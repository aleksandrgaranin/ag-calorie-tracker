from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.

class Food(models.Model):
    def __str__(self):
        return self.name

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    calories = models.IntegerField()

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})

class Consume(models.Model):

    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_concumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    
