
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from notice_board import views as board_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', board_views.SignupView, name='signup'),
    path('accounts/login/', views.LoginView.as_view(), name = 'login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page = '/'), name = 'logout'),
    path('', include('notice_board.urls')),
]
