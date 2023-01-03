from django.urls import path
from App_Login import views

app_name = "App_Login"

urlpatterns = [
    path('edit/', views.edit_profile, name='edit'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
    path('log-sign/', views.log_sign, name='log-sign'),
    path('login/', views.login, name='login'),
]