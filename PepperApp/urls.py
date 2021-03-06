from django.urls import path
from . import views

app_name = "PepperApp"

urlpatterns = [
    path('seoul/', views.seoul, name='seoul'),
    path('busan/', views.busan, name='busan'),
    path('daegu/', views.daegu, name='daegu'),
    path('daejeon/', views.daejeon, name='daejeon'),
    path('gwangju/', views.gwangju, name='gwangju'),
]