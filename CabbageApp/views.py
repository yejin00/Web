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
    
    high_1 = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=1).values_list('도매가격', flat=True)[0]
    high_2 = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=2).values_list('도매가격', flat=True)[0]
    high_3 = Cabbage.objects.filter(부산=1, 배추상품=1 , 년=2021, 월=3).values_list('도매가격', flat=True)[0]
    high_4 = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=4).values_list('도매가격', flat=True)[0]
    high_5 = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=5).values_list('도매가격', flat=True)[0]
    high_6 = Cabbage.objects.filter(부산=1, 배추상품=1 , 년=2021, 월=6).values_list('도매가격', flat=True)[0]
    high_7 = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=7).values_list('도매가격', flat=True)[0]
    high_8 = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=8).values_list('도매가격', flat=True)[0]
    high_9 = Cabbage.objects.filter(부산=1, 배추상품=1 , 년=2021, 월=9).values_list('도매가격', flat=True)[0]
    high_10 = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=10).values_list('도매가격', flat=True)[0]
    high_11 = Cabbage.objects.filter(부산=1, 배추상품=1, 년=2021, 월=11).values_list('도매가격', flat=True)[0]
    high_12 = Cabbage.objects.filter(부산=1, 배추상품=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    
    mean_1 = Cabbage.objects.filter(부산=1, 배추상중=1, 년=2021, 월=1).values_list('도매가격', flat=True)[0]
    mean_2 = Cabbage.objects.filter(부산=1, 배추상중=1, 년=2021, 월=2).values_list('도매가격', flat=True)[0]
    mean_3 = Cabbage.objects.filter(부산=1, 배추상중=1 , 년=2021, 월=3).values_list('도매가격', flat=True)[0]
    mean_4 = Cabbage.objects.filter(부산=1, 배추상중=1, 년=2021, 월=4).values_list('도매가격', flat=True)[0]
    mean_5 = Cabbage.objects.filter(부산=1, 배추상중=1, 년=2021, 월=5).values_list('도매가격', flat=True)[0]
    mean_6 = Cabbage.objects.filter(부산=1, 배추상중=1 , 년=2021, 월=6).values_list('도매가격', flat=True)[0]
    mean_7 = Cabbage.objects.filter(부산=1, 배추상중=1, 년=2021, 월=7).values_list('도매가격', flat=True)[0]
    mean_8 = Cabbage.objects.filter(부산=1, 배추상중=1, 년=2021, 월=8).values_list('도매가격', flat=True)[0]
    mean_9 = Cabbage.objects.filter(부산=1, 배추상중=1 , 년=2021, 월=9).values_list('도매가격', flat=True)[0]
    mean_10 = Cabbage.objects.filter(부산=1, 배추상중=1, 년=2021, 월=10).values_list('도매가격', flat=True)[0]
    mean_11 = Cabbage.objects.filter(부산=1, 배추상중=1, 년=2021, 월=11).values_list('도매가격', flat=True)[0]
    mean_12 = Cabbage.objects.filter(부산=1, 배추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {
        'high' : high, 'middle' : middle, 'mean' : mean,
        'high_1' : high_1, 'high_2' : high_2, 'high_3' : high_3, 'high_4' : high_4, 'high_5' : high_5, 'high_6' : high_6,
        'high_7' : high_7, 'high_8' : high_8, 'high_9' : high_9, 'high_10' : high_10, 'high_11' : high_11, 'high_12' : high_12,
        'mean_1' : mean_1, 'mean_2' : mean_2, 'mean_3' : mean_3, 'mean_4' : mean_4, 'mean_5' : mean_5, 'mean_6' : mean_6,
        'mean_7' : mean_7, 'mean_8' : mean_8, 'mean_9' : mean_9, 'mean_10' : mean_10, 'mean_11' : mean_11, 'mean_12' : mean_12,
        }
    return render(request, 'CabbageApp/busan.html', context)

def daegu(request):
    high = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    middle = Cabbage.objects.filter(대구=1, 배추중품=1, 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    mean = Cabbage.objects.filter(대구=1, 배추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    
    high_1 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=1).values_list('도매가격', flat=True)[0]
    high_2 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=2).values_list('도매가격', flat=True)[0]
    high_3 = Cabbage.objects.filter(대구=1, 배추상품=1 , 년=2021, 월=3).values_list('도매가격', flat=True)[0]
    high_4 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=4).values_list('도매가격', flat=True)[0]
    high_5 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=5).values_list('도매가격', flat=True)[0]
    high_6 = Cabbage.objects.filter(대구=1, 배추상품=1 , 년=2021, 월=6).values_list('도매가격', flat=True)[0]
    high_7 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=7).values_list('도매가격', flat=True)[0]
    high_8 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=8).values_list('도매가격', flat=True)[0]
    high_9 = Cabbage.objects.filter(대구=1, 배추상품=1 , 년=2021, 월=9).values_list('도매가격', flat=True)[0]
    high_10 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=10).values_list('도매가격', flat=True)[0]
    high_11 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=11).values_list('도매가격', flat=True)[0]
    high_12 = Cabbage.objects.filter(대구=1, 배추상품=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    
    mean_1 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=1).values_list('도매가격', flat=True)[0]
    mean_2 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=2).values_list('도매가격', flat=True)[0]
    mean_3 = Cabbage.objects.filter(대구=1, 배추상중=1 , 년=2021, 월=3).values_list('도매가격', flat=True)[0]
    mean_4 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=4).values_list('도매가격', flat=True)[0]
    mean_5 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=5).values_list('도매가격', flat=True)[0]
    mean_6 = Cabbage.objects.filter(대구=1, 배추상중=1 , 년=2021, 월=6).values_list('도매가격', flat=True)[0]
    mean_7 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=7).values_list('도매가격', flat=True)[0]
    mean_8 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=8).values_list('도매가격', flat=True)[0]
    mean_9 = Cabbage.objects.filter(대구=1, 배추상중=1 , 년=2021, 월=9).values_list('도매가격', flat=True)[0]
    mean_10 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=10).values_list('도매가격', flat=True)[0]
    mean_11 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=11).values_list('도매가격', flat=True)[0]
    mean_12 = Cabbage.objects.filter(대구=1, 배추상중=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    context = {
        'high' : high, 'middle' : middle, 'mean' : mean,
        'high_1' : high_1, 'high_2' : high_2, 'high_3' : high_3, 'high_4' : high_4, 'high_5' : high_5, 'high_6' : high_6,
        'high_7' : high_7, 'high_8' : high_8, 'high_9' : high_9, 'high_10' : high_10, 'high_11' : high_11, 'high_12' : high_12,
        'mean_1' : mean_1, 'mean_2' : mean_2, 'mean_3' : mean_3, 'mean_4' : mean_4, 'mean_5' : mean_5, 'mean_6' : mean_6,
        'mean_7' : mean_7, 'mean_8' : mean_8, 'mean_9' : mean_9, 'mean_10' : mean_10, 'mean_11' : mean_11, 'mean_12' : mean_12,
        }
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

def popup(request):
    return render(request, 'CabbageApp/popup.html')