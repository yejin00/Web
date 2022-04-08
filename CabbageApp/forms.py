from django import forms

class CabbageForm(forms.Form):
    년 = forms.DecimalField(label='년')
    월 = forms.DecimalField(label='월')
    배추상품 = forms.DecimalField(label='배추상품')
    배추중품 = forms.DecimalField(label='배추중품')
    서울 = forms.DecimalField(label='서울')
    부산 = forms.DecimalField(label='부산')
    대구 =forms.DecimalField(label='대구')
    광주 = forms.DecimalField(label='광주')
    대전 = forms.DecimalField(label='대전') 
    면적 =forms.DecimalField(label='면적')
    생산량 =forms.DecimalField(label='생산량')
    물가지수 =forms.DecimalField(label='물가지수')
    총지수전년동월비= forms.DecimalField(label='총지수전년동월비')
    신선식품지수전년동월비= forms.DecimalField(label='신선식품지수전년동월비')
    평균기온 = forms.DecimalField(label='평균기온')
    평균최고기온 = forms.DecimalField(label='평균최고기온')
    평균최저기온= forms.DecimalField(label='평균최저기온')
    평균상대습도= forms.DecimalField(label='평균상대습도')
    평균풍속 = forms.DecimalField(label='평균풍속')
    월합강수량= forms.DecimalField(label='월합강수량')
    총지수전년누계비 =forms.DecimalField(label='총지수전년누계비')
    신선식품지수전년누계비 =forms.DecimalField(label='신선식품지수전년누계비')
    배추상중 = forms.DecimalField(label='배추상중')
    

class PopupForm6(forms.Form):
    # 지역 =forms.DecimalField(label='지역', initial='부산')
    면적 =forms.DecimalField(label='면적', initial=6)
    생산량 =forms.DecimalField(label='생산량', initial=771)
    물가지수 =forms.DecimalField(label='물가지수', initial=136)
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