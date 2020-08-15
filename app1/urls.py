from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.page1,name='page1'),         #home page ka path
    path('page2/',views.login,name='login'),   #page 2 login page
    path('page3/',views.logout,name='logout')  #page 3 logout page
]