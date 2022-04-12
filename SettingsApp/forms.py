from django import forms

class PopupForm6(forms.Form):
    면적 =forms.DecimalField(label='면적')# , initial=6)
    생산량 =forms.DecimalField(label='생산량', initial=771)
    물가지수 =forms.DecimalField(label='물가지수' , initial=136)
    평균기온 = forms.DecimalField(label='평균기온', initial=-1.5)
    평균최고기온 = forms.DecimalField(label='평균최고기온', initial=2.842857)
    평균최저기온= forms.DecimalField(label='평균최저기온', initial=-5.471429)
    평균상대습도= forms.DecimalField(label='평균상대습도', initial=52.8)
    월합강수량= forms.DecimalField(label='월합강수량', initial=239.229)
    총지수전년누계비 =forms.DecimalField(label='총지수전년누계비', initial=10)
    

class PopupForm7(forms.Form):
    면적 =forms.DecimalField(label='면적', initial=6)
    생산량 =forms.DecimalField(label='생산량', initial=771)
    물가지수 =forms.DecimalField(label='물가지수', initial=136)
    평균기온 = forms.DecimalField(label='평균기온', initial=-1.5)
    평균최고기온 = forms.DecimalField(label='평균최고기온', initial=2.842857)
    평균최저기온= forms.DecimalField(label='평균최저기온', initial=-5.471429)
    평균상대습도= forms.DecimalField(label='평균상대습도', initial=52.8)
    월합강수량= forms.DecimalField(label='월합강수량', initial=239.229)
    총지수전년누계비 =forms.DecimalField(label='총지수전년누계비', initial=10)
    
    
class PopupForm8(forms.Form):
    면적 =forms.DecimalField(label='면적', initial=6)
    생산량 =forms.DecimalField(label='생산량', initial=771)
    물가지수 =forms.DecimalField(label='물가지수', initial=136)
    평균기온 = forms.DecimalField(label='평균기온', initial=-1.5)
    평균최고기온 = forms.DecimalField(label='평균최고기온', initial=2.842857)
    평균최저기온= forms.DecimalField(label='평균최저기온', initial=-5.471429)
    평균상대습도= forms.DecimalField(label='평균상대습도', initial=52.8)
    월합강수량= forms.DecimalField(label='월합강수량', initial=239.229)
    총지수전년누계비 =forms.DecimalField(label='총지수전년누계비', initial=10)