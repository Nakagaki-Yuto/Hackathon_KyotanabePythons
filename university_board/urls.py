
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('', include('notice_board.urls')),
]
