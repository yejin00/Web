from django.urls import path
from . import views

app_name = "CabbageApp"

urlpatterns = [
    path('seoul/', views.seoul, name='seoul'),
    path('busan/', views.busan, name='busan'),
    path('daegu/', views.daegu, name='daegu'),
    path('daejeon/', views.daejeon, name='daejeon'),
    path('gwangju/', views.gwangju, name='gwangju'),
    path('settings/', views.popup, name='settings'),
    path('form_test/', views.form_test, name='form_test')
]