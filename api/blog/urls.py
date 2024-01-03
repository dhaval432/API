from django.urls import path
from rajan.views import *
urlpatterns = [
    path('getData/',getData)
]