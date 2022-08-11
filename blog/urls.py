from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
   
#    path('<int:pk>/', views.single_post_page),
#    path('', views.index),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('',views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]