"""DjangoPythonWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MeetingsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome',views.welcome),
    path('', views.welcome, name='welcomeurl'),
    path('Date',views.date),
    path("About", views.about),
    #path("meetingView/<int:id>", detail),  # http://127.0.0.1:8000/meetingView/1
    path("website/<int:id>views", views.detail, name='detailurl'),  #http://127.0.0.1:8000/website/1
    path("Rooms", views.listrooms, name='roomurl'),
    path("Rooms/<int:id>", views.roomdetail, name='roomdetailurl'),
    path("NewMeeting", views.addmeetings, name="addmeetingurl")
    #path('meetings/',include('meetings.urls')),   # will include the urls.py under the folder meetings
]
