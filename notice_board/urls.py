from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToppageView, name='top'),
    path('profile/', views.ProfileView, name='profile'),
]