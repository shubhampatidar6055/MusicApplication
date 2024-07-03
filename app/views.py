from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def category(request):
    return render(request,"category.html")

def addsong(request):
    return render(request, "addsong.html")
