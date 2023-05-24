from django.http import HttpResponse


def index(request):
    return HttpResponse('Даша молодец!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
