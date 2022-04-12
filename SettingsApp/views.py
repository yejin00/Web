from django.shortcuts import render
from .models import Cab6, Cab7, Cab8
from .forms import PopupForm6, PopupForm7, PopupForm8

def busan(request): # Cabbage Busan
    if request.method == 'POST':
        form6 = PopupForm6(request.POST, prefix='form6'
                           # , initial={'지역' : '부산', '면적': 36, '생산량': 4017, '물가지수': 136, 
                           # '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, 
                           # '월합강수량': 239.229, '총지수전년누계비': 10}
                           )
        
        form7 = PopupForm7(request.POST, prefix='form7'
                           # , initial={'면적': 36, '생산량': 4017, '물가지수': 136,  
                           # '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, 
                           # '월합강수량': 239.229, 
                           # '총지수전년누계비': 10}
                           )
        
        form8 = PopupForm8(request.POST, prefix='form8'
                           # , initial={'면적': 36, '생산량': 4017, '물가지수': 136, 
                           # '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, 
                           # '월합강수량': 239.229, '총지수전년누계비': 10}
                           )
        
        지역 = Cab6.objects.filter(지역 = '부산').values_list('지역', flat=True)[0]

        if form6.is_valid() and form7.is_valid() and form8.is_valid():
            # update DB, Cab6
            면적 = form6.cleaned_data['면적']
            생산량 =form6.cleaned_data['생산량']
            물가지수 = form6.cleaned_data['물가지수']
            평균기온 = form6.cleaned_data['평균기온']
            평균최고기온 = form6.cleaned_data['평균최고기온']
            평균최저기온= form6.cleaned_data['평균최저기온']
            평균상대습도= form6.cleaned_data['평균상대습도']
            월합강수량= form6.cleaned_data['월합강수량']
            총지수전년누계비 = form6.cleaned_data['총지수전년누계비']   
            model6 = Cab6(지역=지역, 면적=면적, 생산량=생산량, 물가지수=물가지수,
                          평균기온=평균기온, 평균최고기온=평균최고기온, 평균최저기온=평균최저기온, 평균상대습도=평균상대습도, 
                          월합강수량=월합강수량, 총지수전년누계비=총지수전년누계비)                    
            # select row, busan
            model6 = Cab6.objects.get(pk=2)
            model6.면적 = 면적
            model6.생산량 = 생산량
            model6.물가지수 = 물가지수
            model6.평균기온 = 평균기온
            model6.평균최고기온 = 평균최고기온
            model6.평균최저기온 = 평균최저기온
            model6.평균상대습도 = 평균상대습도
            model6.월합강수량 = 월합강수량
            model6.총지수전년누계비 = 총지수전년누계비
            model6.save()
            
            # update DB, Cab7
            면적 = form7.cleaned_data['면적']
            생산량 =form7.cleaned_data['생산량']
            물가지수 = form7.cleaned_data['물가지수']
            평균기온 = form7.cleaned_data['평균기온']
            평균최고기온 = form7.cleaned_data['평균최고기온']
            평균최저기온= form7.cleaned_data['평균최저기온']
            평균상대습도= form7.cleaned_data['평균상대습도']
            월합강수량= form7.cleaned_data['월합강수량']
            총지수전년누계비 = form7.cleaned_data['총지수전년누계비']   
            model7 = Cab7(지역=지역, 면적=면적, 생산량=생산량, 물가지수=물가지수,
                          평균기온=평균기온, 평균최고기온=평균최고기온, 평균최저기온=평균최저기온, 평균상대습도=평균상대습도, 
                          월합강수량=월합강수량, 총지수전년누계비=총지수전년누계비)
            # select row, busan
            model7 = Cab7.objects.get(pk=2)
            model7.면적 = 면적
            model7.생산량 = 생산량
            model7.물가지수 = 물가지수
            model7.평균기온 = 평균기온
            model7.평균최고기온 = 평균최고기온
            model7.평균최저기온 = 평균최저기온
            model7.평균상대습도 = 평균상대습도
            model7.월합강수량 = 월합강수량
            model7.총지수전년누계비 = 총지수전년누계비
            model7.save()
            
            # update DB, Cab8
            면적 = form8.cleaned_data['면적']
            생산량 =form8.cleaned_data['생산량']
            물가지수 = form8.cleaned_data['물가지수']
            평균기온 = form8.cleaned_data['평균기온']
            평균최고기온 = form8.cleaned_data['평균최고기온']
            평균최저기온= form8.cleaned_data['평균최저기온']
            평균상대습도= form8.cleaned_data['평균상대습도']
            월합강수량= form8.cleaned_data['월합강수량']
            총지수전년누계비 = form8.cleaned_data['총지수전년누계비']   
            model8 = Cab8(지역=지역, 면적=면적, 생산량=생산량, 물가지수=물가지수,
                          평균기온=평균기온, 평균최고기온=평균최고기온, 평균최저기온=평균최저기온, 평균상대습도=평균상대습도, 
                          월합강수량=월합강수량, 총지수전년누계비=총지수전년누계비)
            # select row, busan
            model8 = Cab8.objects.get(pk=2)
            model8.면적 = 면적
            model8.생산량 = 생산량
            model8.물가지수 = 물가지수
            model8.평균기온 = 평균기온
            model8.평균최고기온 = 평균최고기온
            model8.평균최저기온 = 평균최저기온
            model8.평균상대습도 = 평균상대습도
            model8.월합강수량 = 월합강수량
            model8.총지수전년누계비 = 총지수전년누계비
            model8.save()
            context = {'form6' : form6, 'form7' : form7, 'form8' : form8}
            return render(request, 'CabbageApp/popup.html', context)
            
    else:
        form6 = PopupForm6(prefix='form6')
        form7 = PopupForm7(prefix='form7')
        form8 = PopupForm8(prefix='form8', initial={'면적': 36, '생산량': 4017, '물가지수': 136, 
                           '평균기온':-1.5, '평균최고기온':2.842857 , '평균최저기온': -5.471429, '평균상대습도': 52.8, 
                           '월합강수량': 239.229, '총지수전년누계비': 10})
        context = {'form6' : form6, 'form7' : form7, 'form8' : form8}
        return render(request, 'CabbageApp/popup.html', context)
