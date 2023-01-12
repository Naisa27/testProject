from django.shortcuts import render
from .models import Menu


def home(request):
    return render(request, 'sam/home.html', {'menu': Menu.objects.all()})


def get_menu(request, slug):
    print(slug)
