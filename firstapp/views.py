from django.http import HttpResponse


def one(request):
    return HttpResponse("Hello there")


def two(request):
    return HttpResponse("Hello there!!!!")

