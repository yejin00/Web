from django.shortcuts import render

def seoul(request):
    return render(request, 'OnionApp/seoul.html')

def busan(request):
    return render(request, 'OnionApp/busan.html')

def daegu(request):
    return render(request, 'OnionApp/daegu.html')

def daejeon(request):
    return render(request, 'OnionApp/daejeon.html')

def gwangju(request):
    return render(request, 'OnionApp/gwangju.html')