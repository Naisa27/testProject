from django.shortcuts import render
from .models import Menu, Article


def home(request):
    return render(request, 'sam/home.html', {})


def get_menu(request, slug):
    menuPoint = Menu.objects.get(slug=slug)

    ancestors = menuPoint.get_ancestors()
    descendants = menuPoint.get_descendants()
    menu_points = [i.slug for i in descendants]
    menu_points.append(slug)

    articles = Article.objects.filter(menuPoint__slug__in=menu_points).select_related('menuPoint')

    return render(
        request,
        "sam/menuPoint.html",
        {
            "ancestors": ancestors,
            "articles": articles,
            "menuPoint": menuPoint,
         }
    )
