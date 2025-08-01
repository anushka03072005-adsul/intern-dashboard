from django.urls import path
from . import views

urlpatterns = [
    # Frontend pages
    path('', views.login_page, name='login'),
    path('dashboard/', views.dashboard_data, name='dashboard'),
    
    # API endpoints
    path('api/login/', views.api_login, name='api_login'),
    path('api/signup/', views.api_signup, name='api_signup'),
    path('api/dashboard/', views.api_dashboard, name='api_dashboard'),
] 