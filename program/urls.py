from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.inputdata),
    path('result/',views.result, name='result'),

]
