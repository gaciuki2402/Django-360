from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Index(request):
    return HttpResponse ('<h1>Welcome to Grace Software Company </h1>')

def ContactUs(request):
    return HttpResponse("<h1>Contact Us Page</h1>")

def AboutUs(request):
    return HttpResponse("<h1>About Us</h1>")

def Main(request):
    return HttpResponse("<h1>Hello,world.you're at the polls index</h1>")
def info(request):
    return HttpResponse("<h1> Welcome all</h1>")

