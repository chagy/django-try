from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html",{})

def about_view(request,*args, **kwargs):
    # return HttpResponse('<h1>Hello Aboute</h1>')
    return render(request,"about.html",{})

def contact_view(request,*args, **kwargs):
    # return HttpResponse('<h1>Hello Contact</h1>')
    return render(request,"contact.html",{})

def social_view(request,*args, **kwargs):
    # return HttpResponse('<h1>Socail Page</h1>')
    return render(request,"social.html",{})