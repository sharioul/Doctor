from django.shortcuts import render, redirect
from django.http import HttpResponse
def desbord(request):

    return render(request, "home.html")

def contact(request):

    return render(request, "contact.html")
def error(request):
    return render(request,"404.html")

def portfolio(request):
    return render(request,"portfolio-details.html")

def blog(request):
    return render(request,"blog-single.html")