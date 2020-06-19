from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('listar/<int:id>', details, name='details')
    path('listar/<slug>', details, name='details')
]