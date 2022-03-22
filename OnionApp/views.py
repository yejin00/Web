from django.shortcuts import render
from .models import Onion

def seoul(request):
    high = Onion.objects.filter(서울=1, 양파상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Onion.objects.filter(서울=1, 양파중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Onion.objects.filter(서울=1, 양파상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'OnionApp/seoul.html', context)

def busan(request):
    high = Onion.objects.filter(부산=1, 양파상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Onion.objects.filter(부산=1, 양파중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Onion.objects.filter(부산=1, 양파상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'OnionApp/busan.html', context)

def daegu(request):
    high = Onion.objects.filter(대구=1, 양파상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Onion.objects.filter(대구=1, 양파중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Onion.objects.filter(대구=1, 양파상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'OnionApp/daegu.html', context)

def daejeon(request):
    high = Onion.objects.filter(대전=1, 양파상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Onion.objects.filter(대전=1, 양파중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Onion.objects.filter(대전=1, 양파상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'OnionApp/daejeon.html', context)

def gwangju(request):
    high = Onion.objects.filter(광주=1, 양파상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Onion.objects.filter(광주=1, 양파중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Onion.objects.filter(광주=1, 양파상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {'high' : high, 'middle' : middle, 'mean' : mean}
    return render(request, 'OnionApp/gwangju.html', context)