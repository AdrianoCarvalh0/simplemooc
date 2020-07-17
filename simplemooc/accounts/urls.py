from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('cadastrar/', register, name='register'),
    path('', dashboard, name='dashboard'),

    path('nova-senha/', 'password_reset', name='password_reset'),
    path('confirmar-nova-senha/<pk>',password_reset_confirm, name='password_reset_confirm'),
    path('editar/', edit, name='edit'),
    path('editar-senha/', edit_password,name='edit_password'),
]