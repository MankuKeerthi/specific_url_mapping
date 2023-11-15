from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def park(request):
    return render(request,'park.html')
def hyung(request):
    return HttpResponse('<h1>Park Hyung Sik is handsome</h1>')