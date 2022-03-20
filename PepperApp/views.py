from django.shortcuts import render

def seoul(request):
    return render(request, 'PepperApp/seoul.html')

def busan(request):
    return render(request, 'PepperApp/busan.html')

def daegu(request):
    return render(request, 'PepperApp/daegu.html')

def daejeon(request):
    return render(request, 'PepperApp/daejeon.html')

def gwangju(request):
    return render(request, 'PepperApp/gwangju.html')