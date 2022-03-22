from django.shortcuts import render
from .models import Radish

def seoul(request):
    high = Radish.objects.filter(서울=1, 무상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Radish.objects.filter(서울=1, 무중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Radish.objects.filter(서울=1, 무상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'RadishApp/seoul.html', context)

def busan(request):
    high = Radish.objects.filter(부산=1, 무상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Radish.objects.filter(부산=1, 무중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Radish.objects.filter(부산=1, 무상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'RadishApp/busan.html', context)

def daegu(request):
    high = Radish.objects.filter(대구=1, 무상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Radish.objects.filter(대구=1, 무중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Radish.objects.filter(대구=1, 무상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'RadishApp/daegu.html', context)

def daejeon(request):
    high = Radish.objects.filter(대전=1, 무상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Radish.objects.filter(대전=1, 무중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Radish.objects.filter(대전=1, 무상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'RadishApp/daejeon.html', context)

def gwangju(request):
    high = Radish.objects.filter(광주=1, 무상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Radish.objects.filter(광주=1, 무중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Radish.objects.filter(광주=1, 무상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'RadishApp/gwangju.html', context)