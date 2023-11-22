from django.shortcuts import render


# Create your views here.
from django.http import HttpRequest
def lenovo(request):
    return render(request,'lenovo.html')
def dell(reuest):
    return HttpRequest('dell from laptop')