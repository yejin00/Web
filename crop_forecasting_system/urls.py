"""crop_forecasting_system URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('CabbageApp/', include('CabbageApp.urls')),
    # path('RadishApp/', include('RadishApp.urls')),
    path('OnionApp/', include('OnionApp.urls')),
    path('PepperApp/', include('PepperApp.urls')),
    path('seoul_cabbage/', views.seoul_cabbage, name='seoul_cabbage'),
    path('seoul_radish/', views.seoul_radish, name='seoul_radish'),
    path('seoul_pepper/', views.seoul_pepper, name='seoul_pepper'),
    path('seoul_onion/', views.seoul_onion, name='seoul_onion'),
    path('test2/', views.test2, name='test2'),
]
