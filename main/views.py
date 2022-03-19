from tkinter.tix import Tree
from django.shortcuts import render
from .models import Cabbage, Onion, Pepper, Radish, CabbageMean, OnionMean, PepperMean, RadishMean
from .forms import CabbageForm, RadishForm, OnionForm, PepperForm
import joblib
from django.http import JsonResponse

def index(request): #지역별 평균 10, 11, 12월 
    #배추
    high_10 = CabbageMean.objects.filter(년=2021, 월=10).values_list('상_도매가격', flat=True)[0]
    high_11 = CabbageMean.objects.filter(년=2021, 월=11).values_list('상_도매가격', flat=True)[0]
    high_12 = CabbageMean.objects.filter(년=2021, 월=12).values_list('상_도매가격', flat=True)[0]
    cabbage_high_list = [high_10, high_11, high_12]
    middle_10 = CabbageMean.objects.filter(년=2021, 월=10).values_list('중_도매가격', flat=True)[0]
    middle_11 = CabbageMean.objects.filter(년=2021, 월=11).values_list('중_도매가격', flat=True)[0]
    middle_12 = CabbageMean.objects.filter(년=2021, 월=12).values_list('중_도매가격', flat=True)[0]
    cabbage_middle_list = [middle_10, middle_11, middle_12]
    mean_10 = CabbageMean.objects.filter(년=2021, 월=10).values_list('상중_도매가격', flat=True)[0]
    mean_11 = CabbageMean.objects.filter(년=2021, 월=11).values_list('상중_도매가격', flat=True)[0]
    mean_12 = CabbageMean.objects.filter(년=2021, 월=12).values_list('상중_도매가격', flat=True)[0]
    cabbage_mean_list = [mean_10, mean_11, mean_12]
    
    # 건고추
    high_10 = PepperMean.objects.filter(년=2021, 월=10).values_list('상_도매가격', flat=True)[0]
    high_11 = PepperMean.objects.filter(년=2021, 월=11).values_list('상_도매가격', flat=True)[0]
    high_12 = PepperMean.objects.filter(년=2021, 월=12).values_list('상_도매가격', flat=True)[0]
    pepper_high_list = [high_10, high_11, high_12]
    middle_10 = PepperMean.objects.filter(년=2021, 월=10).values_list('중_도매가격', flat=True)[0]
    middle_11 = PepperMean.objects.filter(년=2021, 월=11).values_list('중_도매가격', flat=True)[0]
    middle_12 = PepperMean.objects.filter(년=2021, 월=12).values_list('중_도매가격', flat=True)[0]
    pepper_middle_list = [middle_10, middle_11, middle_12]
    mean_10 = PepperMean.objects.filter(년=2021, 월=10).values_list('상중_도매가격', flat=True)[0]
    mean_11 = PepperMean.objects.filter(년=2021, 월=11).values_list('상중_도매가격', flat=True)[0]
    mean_12 = PepperMean.objects.filter(년=2021, 월=12).values_list('상중_도매가격', flat=True)[0]
    pepper_mean_list = [mean_10, mean_11, mean_12]
    
    # 양파
    high_10 = OnionMean.objects.filter(년=2021, 월=10).values_list('상_도매가격', flat=True)[0]
    high_11 = OnionMean.objects.filter(년=2021, 월=11).values_list('상_도매가격', flat=True)[0]
    high_12 = OnionMean.objects.filter(년=2021, 월=12).values_list('상_도매가격', flat=True)[0]
    onion_high_list = [high_10, high_11, high_12]
    middle_10 = OnionMean.objects.filter(년=2021, 월=10).values_list('중_도매가격', flat=True)[0]
    middle_11 = OnionMean.objects.filter(년=2021, 월=11).values_list('중_도매가격', flat=True)[0]
    middle_12 = OnionMean.objects.filter(년=2021, 월=12).values_list('중_도매가격', flat=True)[0]
    onion_middle_list = [middle_10, middle_11, middle_12]
    mean_10 = OnionMean.objects.filter(년=2021, 월=10).values_list('상중_도매가격', flat=True)[0]
    mean_11 = OnionMean.objects.filter(년=2021, 월=11).values_list('상중_도매가격', flat=True)[0]
    mean_12 = OnionMean.objects.filter(년=2021, 월=12).values_list('상중_도매가격', flat=True)[0]
    onion_mean_list = [mean_10, mean_11, mean_12]
    
    # 무
    high_10 = RadishMean.objects.filter(년=2021, 월=10).values_list('상_도매가격', flat=True)[0]
    high_11 = RadishMean.objects.filter(년=2021, 월=11).values_list('상_도매가격', flat=True)[0]
    high_12 = RadishMean.objects.filter(년=2021, 월=12).values_list('상_도매가격', flat=True)[0]
    radish_high_list = [high_10, high_11, high_12]
    middle_10 = RadishMean.objects.filter(년=2021, 월=10).values_list('중_도매가격', flat=True)[0]
    middle_11 = RadishMean.objects.filter(년=2021, 월=11).values_list('중_도매가격', flat=True)[0]
    middle_12 = RadishMean.objects.filter(년=2021, 월=12).values_list('중_도매가격', flat=True)[0]
    radish_middle_list = [middle_10, middle_11, middle_12]
    mean_10 = RadishMean.objects.filter(년=2021, 월=10).values_list('상중_도매가격', flat=True)[0]
    mean_11 = RadishMean.objects.filter(년=2021, 월=11).values_list('상중_도매가격', flat=True)[0]
    mean_12 = RadishMean.objects.filter(년=2021, 월=12).values_list('상중_도매가격', flat=True)[0]
    radish_mean_list = [mean_10, mean_11, mean_12]

    context = {
        'cabbage_high_list' : cabbage_high_list, 'cabbage_middle_list' : cabbage_middle_list, 'cabbage_mean_list' : cabbage_mean_list,
        'pepper_high_list': pepper_high_list, 'pepper_middle_list': pepper_middle_list, 'pepper_mean_list': pepper_mean_list,
        'onion_high_list': onion_high_list, 'onion_middle_list': onion_middle_list, 'onion_mean_list': onion_mean_list,
        'radish_high_list': radish_high_list, 'radish_middle_list': radish_middle_list, 'radish_mean_list': radish_mean_list,        
        }
    return render(request, 'main/index.html', context)

def test2(request):
    # return render(request, 'main/index.html')
    high_10 = Cabbage.objects.filter(서울=1, 배추상품=1, 년=2021, 월=10).values_list('도매가격', flat=True)
    high_11 = Cabbage.objects.filter(서울=1, 배추상품=1, 년=2021, 월=11).values_list('도매가격', flat=True)
    high_12 = Cabbage.objects.filter(서울=1, 배추상품=1, 년=2021, 월=12).values_list('도매가격', flat=True)
    high_list = [high_10, high_11, high_12] # chart 연결 목적
    # context = {'high_10': high_10, 'high_11' : high_11, 'high_12' : high_12}
    # high_list.append(high_10, high_11, high_12)
    # context = {'high_10':high_10, 'high_11':high_11, 'high_12':high_12}
    # context = {'dtitle1': '메롱', 'high_list' : high_list}
    return render(request, 'main/test2.html', {
        'dtitle1': '메롱', 
        'dtitle2': '빵',
        'high_list' : high_list
        })



def seoul_cabbage(request):
    high = Cabbage.objects.filter(서울=1, 배추상품=1, 년=2021, 월=12)
    middle = Cabbage.objects.filter(서울=1, 배추중품=1, 년=2021, 월=12)
    mean = Cabbage.objects.filter(서울=1, 배추상중=1 , 년=2021, 월=12)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CabbageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            년 = form.cleaned_data['년']
            월 = form.cleaned_data['월']
            배추상품 = form.cleaned_data['배추상품']
            배추중품 = form.cleaned_data['배추중품']
            서울 = form.cleaned_data['서울']
            부산 = form.cleaned_data['부산']
            대구 = form.cleaned_data['대구']
            광주 = form.cleaned_data['광주']
            대전 = form.cleaned_data['대전']
            면적 =form.cleaned_data['면적']
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
            # Run new features through ML model
            model_features = [
                [년, 월, 배추상품, 배추중품, 서울, 부산, 대구, 광주, 대전, 면적, 생산량,
       물가지수, 총지수전년동월비, 신선식품지수전년동월비, 평균기온, 평균최고기온, 평균최저기온, 평균상대습도, 평균풍속,
       월합강수량, 총지수전년누계비, 신선식품지수전년누계비, 배추상중]]
            ridge = joblib.load('main/ml_model/lasso_cabbage.pkl')
            # loaded_model = pickle.load(open("./iris_model.pkl", 'rb'))
            prediction = ridge.predict(model_features)[0]
            # prediction = "MyPrediction"

            return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form, 'prediction': prediction})
        
            # if a GET (or any other method) we'll create a blank form
    else:
        form = CabbageForm()

    return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form})


def seoul_radish(request):
    # crops=Crop.objects.all()
    high = Radish.objects.filter(서울=1, 무상품=1, 년=2021, 월=12)
    middle = Radish.objects.filter(서울=1, 무중품=1, 년=2021, 월=12)
    mean = Radish.objects.filter(서울=1, 무상중=1, 년=2021, 월=12)
    # return render(request, 'main\cost2.html', context)

    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
        form = RadishForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            년 = form.cleaned_data['년']
            월 = form.cleaned_data['월']
            무상품 = form.cleaned_data['무상품']
            무중품 = form.cleaned_data['무중품']
            서울 = form.cleaned_data['서울']
            부산 = form.cleaned_data['부산']
            대구 = form.cleaned_data['대구']
            광주 = form.cleaned_data['광주']
            대전 = form.cleaned_data['대전']
            면적 =form.cleaned_data['면적']
            생산량 =form.cleaned_data['생산량']
            물가지수 = form.cleaned_data['물가지수']
            총지수전년누계비 = form.cleaned_data['총지수전년누계비']
            신선식품지수전년누계비 = form.cleaned_data['신선식품지수전년누계비']
            평균기온 = form.cleaned_data['평균기온']
            평균최고기온 = form.cleaned_data['평균최고기온']
            평균최저기온= form.cleaned_data['평균최저기온']
            평균상대습도= form.cleaned_data['평균상대습도']
            월합강수량= form.cleaned_data['월합강수량']
            총지수전년동월비= form.cleaned_data['총지수전년동월비']
            신선식품지수전년동월비= form.cleaned_data['신선식품지수전년동월비']
            무상중 = form.cleaned_data['무상중']
            # Run new features through ML model
            model_features = [
                [년, 월, 무상품, 무중품, 서울, 부산, 대구, 광주, 대전, 면적, 생산량,
       물가지수, 총지수전년누계비, 신선식품지수전년누계비, 평균기온, 평균최고기온, 평균최저기온, 평균상대습도,
       월합강수량, 총지수전년동월비, 신선식품지수전년동월비, 무상중]]
            lasso_radish = joblib.load('main/ml_model/lasso_radish.pkl')
            # loaded_model = pickle.load(open("./iris_model.pkl", 'rb'))
            prediction = lasso_radish.predict(model_features)[0]
            # prediction = "MyPrediction"

            return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form, 'prediction': prediction})
        
            # if a GET (or any other method) we'll create a blank form
    else:
        form = RadishForm()

    return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form})



def seoul_onion(request):
    high = Onion.objects.filter(서울=1, 양파상품=1, 년=2021, 월=12)
    middle = Onion.objects.filter(서울=1, 양파중품=1, 년=2021, 월=12)
    mean =  Onion.objects.filter(서울=1, 양파상중=1, 년=2021, 월=12)

    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
        form = OnionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            년 = form.cleaned_data['년']
            월 = form.cleaned_data['월']
            양파상품 = form.cleaned_data['양파상품']
            양파중품 = form.cleaned_data['양파중품']
            서울 = form.cleaned_data['서울']
            부산 = form.cleaned_data['부산']
            대구 = form.cleaned_data['대구']
            광주 = form.cleaned_data['광주']
            대전 = form.cleaned_data['대전']
            면적 =form.cleaned_data['면적']
            생산량 =form.cleaned_data['생산량']
            물가지수 = form.cleaned_data['물가지수']
            총지수전년누계비 = form.cleaned_data['총지수전년누계비']
            신선식품지수전년누계비 = form.cleaned_data['신선식품지수전년누계비']
            평균기온 = form.cleaned_data['평균기온']
            평균최고기온 = form.cleaned_data['평균최고기온']
            평균최저기온= form.cleaned_data['평균최저기온']
            평균상대습도= form.cleaned_data['평균상대습도']
            월합강수량= form.cleaned_data['월합강수량']
            총지수전년동월비= form.cleaned_data['총지수전년동월비']
            신선식품지수전년동월비= form.cleaned_data['신선식품지수전년동월비']
            양파상중 = form.cleaned_data['양파상중']
            # Run new features through ML model
            model_features = [
                [년, 월, 양파상품, 양파중품, 서울, 부산, 대구, 광주, 대전, 면적, 생산량,
       물가지수, 총지수전년누계비, 신선식품지수전년누계비, 평균기온, 평균최고기온, 평균최저기온, 평균상대습도,
       월합강수량, 총지수전년동월비, 신선식품지수전년동월비, 양파상중]]
            ridge = joblib.load('main/ml_model/ridge_model.pkl')
            # loaded_model = pickle.load(open("./iris_model.pkl", 'rb'))
            prediction = ridge.predict(model_features)[0]
            # prediction = "MyPrediction"

            return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form, 'prediction': prediction})
        
            # if a GET (or any other method) we'll create a blank form
    else:
        form = OnionForm()

    return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form})




def seoul_pepper(request):
    high = Pepper.objects.filter(서울=1, 건고추상품=1, 년=2021, 월=12)
    middle = Pepper.objects.filter(서울=1, 건고추중품=1, 년=2021, 월=12)
    mean = Pepper.objects.filter(서울=1, 건고추상중=1, 년=2021, 월=12)


    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PepperForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            년 = form.cleaned_data['년']
            월 = form.cleaned_data['월']
            건고추상품 = form.cleaned_data['건고추상품']
            건고추중품 = form.cleaned_data['건고추중품']
            서울 = form.cleaned_data['서울']
            부산 = form.cleaned_data['부산']
            대구 = form.cleaned_data['대구']
            광주 = form.cleaned_data['광주']
            대전 = form.cleaned_data['대전']
            면적 =form.cleaned_data['면적']
            생산량 =form.cleaned_data['생산량']
            물가지수 = form.cleaned_data['물가지수']
            총지수전년동월비= form.cleaned_data['총지수전년동월비']
            # 신선식품지수전년동월비= form.cleaned_data['신선식품지수전년동월비']
            # 평균기온 = form.cleaned_data['평균기온']
            # 평균최고기온 = form.cleaned_data['평균최고기온']
            # 평균최저기온= form.cleaned_data['평균최저기온']
            # 평균상대습도= form.cleaned_data['평균상대습도']
            # 평균풍속 = form.cleaned_data['평균풍속']
            # 월합강수량= form.cleaned_data['월합강수량']
            펑균풍속 = form.cleaned_data['평균풍속']
            총지수전년누계비 = form.cleaned_data['총지수전년누계비']
            # 신선식품지수전년누계비 = form.cleaned_data['신선식품지수전년누계비']
            건고추상중 = form.cleaned_data['건고추상중']
            # Run new features through ML model
            model_features = [
                [년, 월, 건고추상품, 건고추중품, 서울, 부산, 대구, 광주, 대전, 면적, 생산량,
       물가지수, 총지수전년동월비, 펑균풍속,  총지수전년누계비, 건고추상중]]
            svr = joblib.load('main/ml_model/svr_model.pkl')
            # loaded_model = pickle.load(open("./iris_model.pkl", 'rb'))
            prediction = svr.predict(model_features)[0]
            # prediction = "MyPrediction"

            return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form, 'prediction': prediction})
        
            # if a GET (or any other method) we'll create a blank form
    else:
        form = PepperForm()

    return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form})
