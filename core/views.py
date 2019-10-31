from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>mi weeeeb.</h1><h2>portadaaaaaaa.</h2>")
