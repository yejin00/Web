from django.shortcuts import render

def seoul(request):
    return render(request, 'RadishApp/seoul.html')

def busan(request):
    return render(request, 'RadishApp/busan.html')

def daegu(request):
    return render(request, 'RadishApp/daegu.html')

def daejeon(request):
    return render(request, 'RadishApp/daejeon.html')

def gwangju(request):
    return render(request, 'RadishApp/gwangju.html')