from django.shortcuts import render

# Create your views here.

def hai(request):

    return render(request,'hai.html')

def hello(requet):
    return render(requet,'hello.html')