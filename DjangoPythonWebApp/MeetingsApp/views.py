from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    #return HttpResponse("Welcome to Meeting Planner!")
    return render(request,"website/welcome.html")


def date(request):
    return HttpResponse("This page is served at " + str(datetime.now()))

def about(request):
    return HttpResponse("About Page")

# Create your views here.
