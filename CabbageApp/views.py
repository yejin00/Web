from django.shortcuts import render

def seoul(request):
    return render(request, 'CabbageApp/seoul.html')

def busan(request):
    return render(request, 'CabbageApp/busan.html')

def daegu(request):
    return render(request, 'CabbageApp/daegu.html')

def daejeon(request):
    return render(request, 'CabbageApp/daejeon.html')

def gwangju(request):
    return render(request, 'CabbageApp/gwangju.html')