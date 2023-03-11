from django.http import HttpResponse


def one(request):
    return HttpResponse("Hello there")

