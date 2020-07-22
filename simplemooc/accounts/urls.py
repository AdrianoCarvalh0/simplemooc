from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('cadastrar/', register, name='register'),
    path('', dashboard, name='dashboard'),
    path('editar-senha/', edit_password, name='edit_password'),
    path('editar-usuario/', edit_user, name='edit_user'),
]