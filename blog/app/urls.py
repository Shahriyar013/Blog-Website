from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('login/', views.loginuser),
    path('create/', views.create),
    path('post/<int:id>/', views.detail),
    path('comment/<int:id>/', views.comment),
    path('like/<int:id>/', views.like),
]