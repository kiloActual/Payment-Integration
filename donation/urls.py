from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.donate,name='donate'),
    path('pay',views.pay,name='pay'),
    path('success/',views.success,name='success'),
]
