from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
    print("indexView: exec")
    return HttpResponse("Hello, World")
