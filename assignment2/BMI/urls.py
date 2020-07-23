from django.urls import path
from .views import index,BMI

urlpatterns = [
    path('',index,name='index'),
    path('BMI/',BMI,name='BMI'),
    #path('ans/',ans,name='ans')
    ]