from django.shortcuts import render
from .models import Cabbage, Onion, Pepper, Radish
from .forms import CabbageForm
import joblib

def index(request):
    # return render(request, 'main/index.html')
    high_10 = Cabbage.objects.filter(서울=1, 배추상품=1, 년=2021, 월=10)
    high_11 = Cabbage.objects.filter(서울=1, 배추상품=1, 년=2021, 월=11)
    high_12 = Cabbage.objects.filter(서울=1, 배추상품=1, 년=2021, 월=12)
    high_list = [high_10, high_11, high_12] # chart 연결 목적
    context = {'high_list': high_list}
    # high_list.append(high_10, high_11, high_12)
    # context = {'high_10':high_10, 'high_11':high_11, 'high_12':high_12}
    return render(request, 'main/index.html', context)

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
            ridge = joblib.load('Web/main/ml_model/ridge_model.pkl')
            # loaded_model = pickle.load(open("./iris_model.pkl", 'rb'))
            prediction = ridge.predict(model_features)[0]
            # prediction = "MyPrediction"

            return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form, 'prediction': prediction})
        
            # if a GET (or any other method) we'll create a blank form
    else:
        form = CabbageForm()

    return render(request, 'main/test.html', {'high' : high, 'middle' : middle, 'mean' : mean, 'form': form})
