from . import views
from django.urls import path
from django.contrib.auth import views as log_views

urlpatterns = [
    path('', log_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', log_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="homepage"),
    path('navbar/', views.navbar),
    
]
