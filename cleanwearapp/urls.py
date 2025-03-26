
from django.contrib import admin
from django.urls import path
from cleanwearapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('starter/', views.starter, name='starter'),
]
