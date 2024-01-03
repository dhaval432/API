from django.urls import path
from rajan.views import *
urlpatterns = [
    
    path('get_data/',getData, name='get_data'),
]