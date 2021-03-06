"""webmundo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('anime',views.anime, name="anime"),
    path('emision',views.emision, name="emision"),
    path('genero',views.tienda, name="genero"),
    path('contacto',views.contacto, name="contacto"),
    path('tienda',views.tienda, name="tienda"),
    path('blog',views.blog, name="blog"),
    path('servicios',views.servicios, name="servicios"),
]