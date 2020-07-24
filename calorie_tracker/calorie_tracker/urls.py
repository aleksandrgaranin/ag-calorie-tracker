"""calorie_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calories import views as calories_veiws
from users import views as users_views
from django.contrib.auth import views as authentication_viws


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calories_veiws.welcome, name='welcome'),
    path('index/',calories_veiws.index, name='index'),
    path('delete/<int:id>/', calories_veiws.delete_consume,name='delete'),
    path('register/', users_views.register, name='register'),
    path('login/', authentication_viws.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', authentication_viws.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',users_views.profilepage, name='profile'),
    # add item
    path('add/',calories_veiws.CreateFood.as_view(),name='reate_item'),
    # edit
    path('update/<int:id>/',calories_veiws.update_food,name='update_food'),
    # delete
    path('delete/<int:id>/',calories_veiws.delete_food,name='delete_food'),
    # detail
    path('<int:pk>/',calories_veiws.DetaleClassView.as_view(),name='detail'),
]
