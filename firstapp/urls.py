from django.urls import path

from .views import *

urlpatterns = [
    path('one/', one),
    path('two/', two)
]
