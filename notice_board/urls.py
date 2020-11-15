from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToppageView, name='top'),
    path('profile/', views.ProfileView, name='profile'),
    path('thread/<int:pk>/', views.ThreadDetailView, name='thread_detail'),
    path('thread/<int:pk>/post/', views.AddPostView, name='add_post'),
    path('category/<int:pk>/', views.ThreadListView, name='thread_list'),
    path('thread/add/', views.AddThreadView, name='add_thread'),
    path('report/<int:pk>/', views.ReportView, name='report'),

]