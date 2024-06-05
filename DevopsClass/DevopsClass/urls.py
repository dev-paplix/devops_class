"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from DockerDevops.views import add_name, saved_names

urlpatterns = [
    #App API
    path('add_name/', add_name.as_view(), name="add_name"),
    path('saved_names', saved_names.as_view(), name="saved_names"),

  
]

