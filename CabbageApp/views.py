from cgi import test
from multiprocessing import context
from pickle import GET
from pyexpat import model
from django.shortcuts import render, redirect
from .models import Cabbage, Test
import joblib
from .forms import CabbageForm, PopupForm

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

    
    if request.method == 'GET':
        test = Test.objects.all()
        if test.exists():
            면적 = Test.objects.values_list('면적', flat=True)[0]
            생산량 = Test.objects.values_list('생산량', flat=True)[0]
            물가지수 = Test.objects.values_list('물가지수', flat=True)[0]
            총지수전년동월비 = Test.objects.values_list('총지수전년동월비', flat=True)[0]
            신선식품지수전년동월비 = Test.objects.values_list('신선식품지수전년동월비', flat=True)[0]
            평균기온 = Test.objects.values_list('평균기온', flat=True)[0]
            평균최고기온 = Test.objects.values_list('평균최고기온', flat=True)[0]
            평균최저기온 = Test.objects.values_list('평균최저기온', flat=True)[0]
            평균풍속 = Test.objects.values_list('평균풍속', flat=True)[0]
            월합강수량 = Test.objects.values_list('월합강수량', flat=True)[0]
            평균상대습도 = Test.objects.values_list('평균상대습도', flat=True)[0]
            총지수전년누계비 = Test.objects.values_list('총지수전년누계비', flat=True)[0]
            신선식품지수전년누계비 = Test.objects.values_list('신선식품지수전년누계비', flat=True)[0]
      
            data_high = {'년': 2022, '월': 1, '배추상품' : 1, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                        '면적': 면적, '생산량': 생산량, '물가지수': 물가지수, '총지수전년동월비': 총지수전년동월비, '신선식품지수전년동월비': 신선식품지수전년동월비, 
                        '평균기온': 평균기온, '평균최고기온': 평균최고기온, '평균최저기온': 평균최저기온, '평균상대습도': 평균상대습도, '평균풍속': 평균풍속, '월합강수량': 월합강수량,
                        '총지수전년누계비': 총지수전년누계비, '신선식품지수전년누계비':신선식품지수전년누계비, '배추상중': 0,}
            
            data_middle = {'년': 2022, '월': 1, '배추상품' : 0, '배추중품': 1, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, '면적': 면적, '생산량': 생산량, '물가지수': 물가지수, '총지수전년동월비': 총지수전년동월비, '신선식품지수전년동월비': 신선식품지수전년동월비, 
                        '평균기온': 평균기온, '평균최고기온': 평균최고기온, '평균최저기온': 평균최저기온, '평균상대습도': 평균상대습도, '평균풍속': 평균풍속, '월합강수량': 월합강수량, 
                        '총지수전년누계비': 총지수전년누계비, '신선식품지수전년누계비':신선식품지수전년누계비, '배추상중': 0,
                        }
            
            data_mean = {'년': 2022, '월': 1, '배추상품' : 0, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                        '면적': 면적, '생산량': 생산량, '물가지수': 물가지수, '총지수전년동월비': 총지수전년동월비, '신선식품지수전년동월비': 신선식품지수전년동월비, 
                        '평균기온': 평균기온, '평균최고기온': 평균최고기온, '평균최저기온': 평균최저기온, '평균상대습도': 평균상대습도, '평균풍속': 평균풍속, '월합강수량': 월합강수량, 
                        '총지수전년누계비': 총지수전년누계비, '신선식품지수전년누계비':신선식품지수전년누계비, '배추상중': 1,
                        }
            
        else: 
            
            data_high = {'년': 2022, '월': 1, '배추상품' : 1, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 6, '생산량': 771, '물가지수': 136, '총지수전년동월비':1.18, '신선식품지수전년동월비':5, 
                    '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, '평균풍속': 2.12, '월합강수량': 239.229, 
                    '총지수전년누계비': 10, '신선식품지수전년누계비':10, '배추상중': 0,
                    }
            data_middle = {'년': 2022, '월': 1, '배추상품' : 0, '배추중품': 1, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 6, '생산량': 771, '물가지수': 136, '총지수전년동월비':1.18, '신선식품지수전년동월비':5, 
                    '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, '평균풍속': 2.12, '월합강수량': 239.229, 
                    '총지수전년누계비': 10, '신선식품지수전년누계비':10, '배추상중': 0,
                    }
            data_mean = {'년': 2022, '월': 1, '배추상품' : 0, '배추중품': 0, '서울' : 0, '부산' : 1, '대구':0, '광주':0, '대전':0, 
                    '면적': 6, '생산량': 771, '물가지수': 136, '총지수전년동월비':1.18, '신선식품지수전년동월비':5, 
                    '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, '평균풍속': 2.12, '월합강수량': 239.229, 
                    '총지수전년누계비': 10, '신선식품지수전년누계비':10, '배추상중': 1,
                    }
            
        data_list = [data_high, data_middle, data_mean]
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
                총지수전년동월비= form.cleaned_data['총지수전년동월비']
                신선식품지수전년동월비= form.cleaned_data['신선식품지수전년동월비']
                평균기온 = form.cleaned_data['평균기온']
                평균최고기온 = form.cleaned_data['평균최고기온']
                평균최저기온= form.cleaned_data['평균최저기온']
                평균상대습도= form.cleaned_data['평균상대습도']
                평균풍속 = form.cleaned_data['평균풍속']
                월합강수량= form.cleaned_data['월합강수량']
                총지수전년누계비 = form.cleaned_data['총지수전년누계비']
                신선식품지수전년누계비 = form.cleaned_data['신선식품지수전년누계비']
                배추상중 = form.cleaned_data['배추상중']
                model_features = [
                    [년, 월, 배추상품, 배추중품, 서울, 부산, 대구, 광주, 대전, 면적, 생산량,
                     물가지수, 총지수전년동월비, 신선식품지수전년동월비, 평균기온, 평균최고기온, 평균최저기온, 평균상대습도, 평균풍속,
                     월합강수량, 총지수전년누계비, 신선식품지수전년누계비, 배추상중]]
                ridge = joblib.load('main/ml_model/lasso_cabbage.pkl')
                default_prediction = ridge.predict(model_features)[0]
                default_prediction = default_prediction.round(3)
                default_list.append(default_prediction)
        
        # prediction value 넣어서 바꿔야함(뒤에 세개)
        high_list = [high_1, high_2, high_3, high_4, high_5, high_6, high_7, high_8, high_9, high_10, high_11, high_12]
        mean_list = [mean_1, mean_2, mean_3, mean_4, mean_5, mean_6, mean_7, mean_8, mean_9, mean_10, mean_11, mean_12]
        
        context = {
        'high' : high, 'middle' : middle, 'mean' : mean,
        'high_list': high_list, 'mean_list': mean_list,
        'default_high': default_list[0], 'default_middle': default_list[1], 'default_mean': default_list[2]
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
    
    
def settings(request):
    
    Test.objects.all().delete()

    if request.method == 'POST':
        form = PopupForm(request.POST, initial={'면적': 6, '생산량': 771, '물가지수': 136, '총지수전년동월비':1.18, '신선식품지수전년동월비':5, 
        '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, '평균풍속': 2.12, '월합강수량': 239.229, 
        '총지수전년누계비': 10, '신선식품지수전년누계비':10})
        
        if form.is_valid():
            model = Test(면적=form.data['면적'], 생산량=form.data['생산량'], 물가지수=form.data['물가지수'], 총지수전년동월비=form.data['총지수전년동월비'],
                       신선식품지수전년동월비=form.data['신선식품지수전년동월비'], 평균기온=form.data['평균기온'], 평균최고기온=form.data['평균최고기온'],
                        평균최저기온=form.data['평균최저기온'], 평균상대습도=form.data['평균상대습도'], 평균풍속=form.data['평균풍속']
                        , 월합강수량=form.data['월합강수량'], 총지수전년누계비=form.data['총지수전년누계비'], 신선식품지수전년누계비=form.data['신선식품지수전년누계비'])           
            model.save()
            return render(request, 'CabbageApp/popup.html', {'form': form})
            
    else:
        Test.objects.all().delete()
        form = PopupForm()
        return render(request, 'CabbageApp/popup.html', {'form': form})
  