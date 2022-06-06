"""soc_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.http import HttpResponse
from django.contrib import admin

from django.urls import path, include

def home(request):
    return HttpResponse("You are about to learn django with Aziza")


def get_aticle(request, id):
    return HttpResponse(f"your id is : {id}")

urlpatterns = [
    path('back/', admin.site.urls),
    path('home/', home),
    path('home/<int:id>', get_aticle),
    path('knowledge/', include("knowledge.urls")),


]
