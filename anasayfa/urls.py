from django.contrib import admin
from django.urls import path
from anasayfa import views

app_name ="anasayfa"

urlpatterns = [
    path('',views.index,name = "index")
]
