from multiprocessing import context
from django.shortcuts import render
from .models import Cabbage

def seoul(request):
    high = Cabbage.objects.filter(서울=1, 배추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Cabbage.objects.filter(서울=1, 배추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Cabbage.objects.filter(서울=1, 배추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'CabbageApp/seoul.html', context)

def busan(request):
    high = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Cabbage.objects.filter(부산=1, 배추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'CabbageApp/busan.html', context)

def daegu(request):
    high = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Cabbage.objects.filter(대구=1, 배추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Cabbage.objects.filter(대구=1, 배추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'CabbageApp/daegu.html', context)

def daejeon(request):
    high = Cabbage.objects.filter(대전=1, 배추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Cabbage.objects.filter(대전=1, 배추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Cabbage.objects.filter(대전=1, 배추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'CabbageApp/daejeon.html', context)

def gwangju(request):
    high = Cabbage.objects.filter(광주=1, 배추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Cabbage.objects.filter(광주=1, 배추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Cabbage.objects.filter(광주=1, 배추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'CabbageApp/gwangju.html', context)