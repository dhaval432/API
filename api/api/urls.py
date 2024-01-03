"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from home.views import  *
# from home.views import login_page, register


urlpatterns = [

    path('admin/', admin.site.urls),
    path('.api/',include('.api.urls')),
    # path('delete_data/<id>/',delete_data , name="delete_data"),
    # path('update_data/<id>/',update_data , name="update_data"), 
     
    # path('/login' , login_page , name="login_page"),
    # path('/register' , register , name="register"),
    
    # path('logout_page' , logout_page , name="logout_page")
        

]




