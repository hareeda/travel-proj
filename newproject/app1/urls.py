from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('add/',views.addition,name='addition'),
    #path('sub/',views.subtraction,name='subtraction'),
    #path('mul/',views.multiplication,name='multiplication'),
    #path('div/',views.division,name='division'),
    #path('',views.demo,name='demo'),

]

