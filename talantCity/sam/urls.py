from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('menu/<str:slug>', get_menu, name='menu'),
]
