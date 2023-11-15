from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cha(request):
    return render(request,'cha.html')
def eun(request):
    return HttpResponse('<h1>Lee Dong Min is very handsome</h1>')
