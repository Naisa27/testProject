import time
from .models import Menu
from django.utils.deprecation import MiddlewareMixin


def test_middleware(get_response):

    def middleware(request):
        start = time.time()
        request.menu = Menu.objects.all()
        response = get_response(request)
        end = time.time()
        print(f'Time: {end - start}')
        return response

    return middleware


class getMenu(MiddlewareMixin):
    def process_request(self, request):
        request.menu = Menu.objects.all()
        return None
