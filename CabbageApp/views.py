from cgi import test
from multiprocessing import context
from pickle import GET
from pyexpat import model
from django.shortcuts import render, redirect
from .models import Cabbage, Test, CabbageBusan, Cab6, Cab7, Cab8
import joblib
from .forms import CabbageForm,  PopupForm6, PopupForm7, PopupForm8

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


    middle_1 = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021, 월=1).values_list('도매가격', flat=True)[0]
    middle_2 = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021, 월=2).values_list('도매가격', flat=True)[0]
    middle_3 = Cabbage.objects.filter(부산=1, 배추중품=1 , 년=2021, 월=3).values_list('도매가격', flat=True)[0]
    middle_4 = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021, 월=4).values_list('도매가격', flat=True)[0]
    middle_5 = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021, 월=5).values_list('도매가격', flat=True)[0]
    middle_6 = Cabbage.objects.filter(부산=1, 배추중품=1 , 년=2021, 월=6).values_list('도매가격', flat=True)[0]
    middle_7 = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021,월=7 ).values_list('도매가격', flat=True)[0]
    middle_8 = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021, 월=8).values_list('도매가격', flat=True)[0]
    middle_9 = Cabbage.objects.filter(부산=1, 배추중품=1 , 년=2021, 월=9).values_list('도매가격', flat=True)[0]
    middle_10 = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021, 월=10).values_list('도매가격', flat=True)[0]
    middle_11 = Cabbage.objects.filter(부산=1, 배추중품=1, 년=2021, 월=11).values_list('도매가격', flat=True)[0]
    middle_12 = Cabbage.objects.filter(부산=1, 배추중품=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    
    if request.method == 'GET':
        
        면적 = Cab6.objects.filter(지역='부산').values_list('면적', flat=True)[0]
        생산량 = Cab6.objects.filter(지역='부산').values_list('생산량', flat=True)[0]
        물가지수6 = Cab6.objects.filter(지역='부산').values_list('물가지수', flat=True)[0]
        평균기온6 = Cab6.objects.filter(지역='부산').values_list('평균기온', flat=True)[0]
        평균최고기온6 = Cab6.objects.filter(지역='부산').values_list('평균최고기온', flat=True)[0]
        평균최저기온6 = Cab6.objects.filter(지역='부산').values_list('평균최저기온', flat=True)[0]
        월합강수량6 = Cab6.objects.filter(지역='부산').values_list('월합강수량', flat=True)[0]
        평균상대습도6 = Cab6.objects.filter(지역='부산').values_list('평균상대습도', flat=True)[0]
        총지수전년누계비6 = Cab6.objects.filter(지역='부산').values_list('총지수전년누계비', flat=True)[0]
        
        물가지수7 = Cab7.objects.filter(지역='부산').values_list('물가지수', flat=True)[0]
        평균기온7 = Cab7.objects.filter(지역='부산').values_list('평균기온', flat=True)[0]
        평균최고기온7 = Cab7.objects.filter(지역='부산').values_list('평균최고기온', flat=True)[0]
        평균최저기온7 = Cab7.objects.filter(지역='부산').values_list('평균최저기온', flat=True)[0]
        월합강수량7 = Cab7.objects.filter(지역='부산').values_list('월합강수량', flat=True)[0]
        평균상대습도7 = Cab7.objects.filter(지역='부산').values_list('평균상대습도', flat=True)[0]
        총지수전년누계비7 = Cab7.objects.filter(지역='부산').values_list('총지수전년누계비', flat=True)[0]
        
        물가지수8 = Cab8.objects.filter(지역='부산').values_list('물가지수', flat=True)[0]
        평균기온8 = Cab8.objects.filter(지역='부산').values_list('평균기온', flat=True)[0]
        평균최고기온8 = Cab8.objects.filter(지역='부산').values_list('평균최고기온', flat=True)[0]
        평균최저기온8 = Cab8.objects.filter(지역='부산').values_list('평균최저기온', flat=True)[0]
        월합강수량8 = Cab8.objects.filter(지역='부산').values_list('월합강수량', flat=True)[0]
        평균상대습도8 = Cab8.objects.filter(지역='부산').values_list('평균상대습도', flat=True)[0]
        총지수전년누계비8 = Cab8.objects.filter(지역='부산').values_list('총지수전년누계비', flat=True)[0]
        
        
        data_high6 = {'년': 2022, '월': 6, '배추상품' : 1, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수6,
                    '평균기온': 평균기온6, '평균최고기온': 평균최고기온6, '평균최저기온': 평균최저기온6, '평균상대습도': 평균상대습도6, '월합강수량': 월합강수량6,
                    '총지수전년누계비': 총지수전년누계비6,  '배추상중': 0,}
        
        data_high7 = {'년': 2022, '월': 7, '배추상품' : 1, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수7,  
                    '평균기온': 평균기온7, '평균최고기온': 평균최고기온7, '평균최저기온': 평균최저기온7, '평균상대습도': 평균상대습도7,  '월합강수량': 월합강수량7,
                    '총지수전년누계비': 총지수전년누계비7, '배추상중': 0,}
        
        data_high8 = {'년': 2022, '월': 8, '배추상품' : 1, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수8, 
                    '평균기온': 평균기온8, '평균최고기온': 평균최고기온8, '평균최저기온': 평균최저기온8, '평균상대습도': 평균상대습도8,  '월합강수량': 월합강수량8,
                    '총지수전년누계비': 총지수전년누계비8,  '배추상중': 0,}
        
        
        
        data_middle6= {'년': 2022, '월': 6, '배추상품' : 0, '배추중품': 1, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수6,
                    '평균기온': 평균기온6, '평균최고기온': 평균최고기온6, '평균최저기온': 평균최저기온6, '평균상대습도': 평균상대습도6,'월합강수량': 월합강수량6,
                    '총지수전년누계비': 총지수전년누계비6, '배추상중': 0,}
        
        data_middle7 = {'년': 2022, '월': 7, '배추상품' : 0, '배추중품':1 , '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수7, 
                    '평균기온': 평균기온7, '평균최고기온': 평균최고기온7, '평균최저기온': 평균최저기온7, '평균상대습도': 평균상대습도7, '월합강수량': 월합강수량7,
                    '총지수전년누계비': 총지수전년누계비7,  '배추상중': 0,}
        
        data_middle8 = {'년': 2022, '월': 8, '배추상품' : 0, '배추중품': 1, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수8, 
                    '평균기온': 평균기온8, '평균최고기온': 평균최고기온8, '평균최저기온': 평균최저기온8, '평균상대습도': 평균상대습도8, '월합강수량': 월합강수량8,
                    '총지수전년누계비': 총지수전년누계비8,  '배추상중': 0,}             
        
        
        
        data_mean6= {'년': 2022, '월': 6, '배추상품' : 0, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수6,   
                    '평균기온': 평균기온6, '평균최고기온': 평균최고기온6, '평균최저기온': 평균최저기온6, '평균상대습도': 평균상대습도6, '월합강수량': 월합강수량6,
                    '총지수전년누계비': 총지수전년누계비6,  '배추상중': 1,}
        
        data_mean7 = {'년': 2022, '월': 7, '배추상품' : 0, '배추중품':0 , '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수7, 
                    '평균기온': 평균기온7, '평균최고기온': 평균최고기온7, '평균최저기온': 평균최저기온7, '평균상대습도': 평균상대습도7,  '월합강수량': 월합강수량7,
                    '총지수전년누계비': 총지수전년누계비7, '배추상중': 1,}
        
        data_mean8 = {'년': 2022, '월': 8, '배추상품' : 0, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 면적, '생산량': 생산량, '물가지수': 물가지수8, 
                    '평균기온': 평균기온8, '평균최고기온': 평균최고기온8, '평균최저기온': 평균최저기온8, '평균상대습도': 평균상대습도8, '월합강수량': 월합강수량8,
                    '총지수전년누계비': 총지수전년누계비8, '배추상중': 1,}   

        
        data_list = [data_high6, data_high7, data_high8,
                     data_middle6, data_middle7, data_middle8,
                     data_mean6, data_mean7, data_mean8
                     ]
        
        default_list = []
        for i in data_list:
            form = CabbageForm(i)
            if form.is_valid():
                년 = form.cleaned_data['년']
                월 = form.cleaned_data['월']
                배추상품 = form.cleaned_data['배추상품']
                배추중품 = form.cleaned_data['배추중품']
                서울 = form.cleaned_data['서울']
                부산 = form.cleaned_data['부산']
                대구 = form.cleaned_data['대구']
                광주 = form.cleaned_data['광주']
                대전 = form.cleaned_data['대전']
                면적 = form.cleaned_data['면적']
                생산량 =form.cleaned_data['생산량']
                물가지수 = form.cleaned_data['물가지수']
                평균기온 = form.cleaned_data['평균기온']
                평균최고기온 = form.cleaned_data['평균최고기온']
                평균최저기온= form.cleaned_data['평균최저기온']
                평균상대습도= form.cleaned_data['평균상대습도']
                월합강수량= form.cleaned_data['월합강수량']
                총지수전년누계비 = form.cleaned_data['총지수전년누계비']
                배추상중 = form.cleaned_data['배추상중']
                model_features = [
                    [년, 월, 배추상품, 배추중품, 서울, 부산, 대구, 광주, 대전, 면적, 생산량,
                     물가지수,평균기온, 평균최고기온, 평균최저기온, 평균상대습도,
                     월합강수량, 총지수전년누계비, 배추상중]]
                ridge = joblib.load('main/ml_model/cabbage_ridge_model.pkl')
                default_prediction = ridge.predict(model_features)[0]
                default_prediction = default_prediction.round(3)
                default_list.append(default_prediction)
        
        # prediction value 넣어서 바꿔야함(뒤에 세개)
        high_list = [high_9, high_10, high_11, high_12, high_1, high_2, high_3, high_4, high_5, default_list[0],  default_list[1], default_list[2]]
        mean_list = [mean_9, mean_10, mean_11, mean_12, mean_1, mean_2, mean_3, mean_4, mean_5, default_list[6],  default_list[7], default_list[8]]
        middle_list = [middle_9, middle_10, middle_11, middle_12, middle_1, middle_2, middle_3, middle_4, middle_5, default_list[3],  default_list[4], default_list[5]]
        
        
        context = {
        'high' : high, 'middle' : middle, 'mean' : mean,
        'high_list': high_list, 'mean_list': mean_list, 'middle_list' : middle_list,
        'default_high': default_list[0], 'default_middle': default_list[3], 'default_mean': default_list[6]
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
    high_6 = Cabbage.objects.filter(대구=1, 배추상품=1 , 년=2021, 지역='부산').values_list('도매가격', flat=True)[0]
    high_7 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, ).values_list('도매가격', flat=True)[0]
    high_8 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 지역='부산').values_list('도매가격', flat=True)[0]
    high_9 = Cabbage.objects.filter(대구=1, 배추상품=1 , 년=2021, 월=9).values_list('도매가격', flat=True)[0]
    high_10 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=10).values_list('도매가격', flat=True)[0]
    high_11 = Cabbage.objects.filter(대구=1, 배추상품=1, 년=2021, 월=11).values_list('도매가격', flat=True)[0]
    high_12 = Cabbage.objects.filter(대구=1, 배추상품=1 , 년=2021, 월=12).values_list('도매가격', flat=True)[0]
    
    mean_1 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=1).values_list('도매가격', flat=True)[0]
    mean_2 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=2).values_list('도매가격', flat=True)[0]
    mean_3 = Cabbage.objects.filter(대구=1, 배추상중=1 , 년=2021, 월=3).values_list('도매가격', flat=True)[0]
    mean_4 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=4).values_list('도매가격', flat=True)[0]
    mean_5 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 월=5).values_list('도매가격', flat=True)[0]
    mean_6 = Cabbage.objects.filter(대구=1, 배추상중=1 , 년=2021, 지역='부산').values_list('도매가격', flat=True)[0]
    mean_7 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, ).values_list('도매가격', flat=True)[0]
    mean_8 = Cabbage.objects.filter(대구=1, 배추상중=1, 년=2021, 지역='부산').values_list('도매가격', flat=True)[0]
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
    
    
def settings(request):
    
    Test.objects.all().delete()

    if request.method == 'POST':
        form6 = PopupForm6(request.POST, initial={'지역' : '부산', '면적': 6, '생산량': 771, '물가지수': 136, 
        '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, '월합강수량': 239.229, 
        '총지수전년누계비': 10})
        
        form7 = PopupForm7(request.POST, initial={'면적': 6, '생산량': 771, '물가지수': 136,  
        '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, '월합강수량': 239.229, 
        '총지수전년누계비': 10, '신선식품지수전년누계비':10})
        
        form8 = PopupForm8(request.POST, initial={'면적': 6, '생산량': 771, '물가지수': 136, 
        '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, '월합강수량': 239.229, 
        '총지수전년누계비': 10, '신선식품지수전년누계비':10})
        
        지역 = Cab6.objects.values_list('지역', flat=True)[0]

        
        if form6.is_valid():
            model = Cab6(지역=지역, 면적=form6.data['면적'], 생산량=form6.data['생산량'], 물가지수=form6.data['물가지수'],
                        평균기온=form6.data['평균기온'], 평균최고기온=form6.data['평균최고기온'],
                        평균최저기온=form6.data['평균최저기온'], 평균상대습도=form6.data['평균상대습도'], 
                        월합강수량=form6.data['월합강수량'], 총지수전년누계비=form6.data['총지수전년누계비'])           
            
            model.objects.filter(id=2).update()
            
            context = {'form6' : form6, 'form7' : form7, 'form8' : form8}
            return render(request, 'CabbageApp/popup.html', context) 
                          
        if form7.is_valid():
            model = Cab7(지역=지역, 면적=form7.data['면적'], 생산량=form7.data['생산량'], 물가지수=form7.data['물가지수'],
                        평균기온=form7.data['평균기온'], 평균최고기온=form7.data['평균최고기온'],
                        평균최저기온=form7.data['평균최저기온'], 평균상대습도=form7.data['평균상대습도'], 
                        월합강수량=form7.data['월합강수량'], 총지수전년누계비=form7.data['총지수전년누계비'])  
            model.save()
            context = {'form6' : form6, 'form7' : form7, 'form8' : form8}
            return render(request, 'CabbageApp/popup.html', context) 
        
        if form8.is_valid():
            model = Cab8(지역=지역, 면적=form8.data['면적'], 생산량=form8.data['생산량'], 물가지수=form8.data['물가지수'],
                        평균기온=form8.data['평균기온'], 평균최고기온=form8.data['평균최고기온'],
                        평균최저기온=form8.data['평균최저기온'], 평균상대습도=form8.data['평균상대습도'], 
                        월합강수량=form8.data['월합강수량'], 총지수전년누계비=form8.data['총지수전년누계비'])
            model.save()
            context = {'form6' : form6, 'form7' : form7, 'form8' : form8}
            return render(request, 'CabbageApp/popup.html', context) 
            
    else:
        Test.objects.all().delete()
        form6 = PopupForm6()
        form7 = PopupForm7()
        form8 = PopupForm8()
        context = {'form6' : form6, 'form7' : form7, 'form8' : form8}
        return render(request, 'CabbageApp/popup.html', context)
  
  