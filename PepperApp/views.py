from django.shortcuts import render
from .models import Pepper

def seoul(request):
    high = Pepper.objects.filter(서울=1, 건고추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Pepper.objects.filter(서울=1, 건고추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Pepper.objects.filter(서울=1, 건고추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'PepperApp/seoul.html', context)

def busan(request):
    high = Pepper.objects.filter(부산=1, 건고추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Pepper.objects.filter(부산=1, 건고추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Pepper.objects.filter(부산=1, 건고추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'PepperApp/busan.html', context)

def daegu(request):
    high = Pepper.objects.filter(대구=1, 건고추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Pepper.objects.filter(대구=1, 건고추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Pepper.objects.filter(대구=1, 건고추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'PepperApp/daegu.html', context)

def daejeon(request):
    high = Pepper.objects.filter(대전=1, 건고추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Pepper.objects.filter(대전=1, 건고추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Pepper.objects.filter(대전=1, 건고추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'PepperApp/daejeon.html', context)

def gwangju(request):
    high = Pepper.objects.filter(광주=1, 건고추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Pepper.objects.filter(광주=1, 건고추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Pepper.objects.filter(광주=1, 건고추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'PepperApp/gwangju.html', context)