from django.db import models
from datetime import time

"""_summary_
Please add a model class called Meetings
    Returns:
        _type_: _description_
"""
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    roomnumber = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} : room {self.roomnumber} on floor {self.floor}"


"""_summary_
Please add a model class called Room
    Returns:
        _type_: _description_
"""
class Meetings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    starttime = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} at {self.starttime} on {self.date}"
        
# Create your models here.
