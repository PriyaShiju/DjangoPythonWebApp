from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from datetime import datetime
from MeetingsApp.models import Meetings,Room
from django.forms import modelform_factory

def welcome(request):
    #return HttpResponse("Welcome to Meeting Planner!")
    return render(request,"website/welcome.html", {"num_meetings":Meetings.objects.count(),
                   "meetings": Meetings.objects.all(),
                   "x":"https://github.com/PriyaShiju?tab=repositories"})


def date(request):
    return HttpResponse("This page is served at " + str(datetime.now()))

def about(request):
    return HttpResponse("About Page")

def detail(request, id):
    #meeting = Meetings.objects.get(pk=id)
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, "website/detail.html", {"meetingvar" : meeting})
    
def listrooms(request):
    return render(request, "website/rooms.html", {"num_rooms": Room.objects.count(),
                                                  "rooms":Room.objects.all()})

def roomdetail(request,id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "website/roomdetail.html", {"roomvar": room })

MeetingForm = modelform_factory(Meetings,exclude=[])

def addmeetings(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
            #return redirect("/welcome")
    else:
        form = MeetingForm()
    return render(request,"website/newmeetings.html", {"form" :form})