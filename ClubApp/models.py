from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClubInformation (models.Model):
    clubname=models.CharField(max_length=255)
    clubdescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.clubname

    class Meta():
        db_table='clubinformation'
        verbose_name_plural='clubinformations'

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle

    class Meta():
        db_table='meeting'
        verbose_name_plural='meetings'

class MeetingMinute(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutes=models.CharField(max_length=255)

    def __str__(self):
        return self.minutes

    class Meta():
        db_table='meetingminute'
        verbose_name_plural='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField(null=True, blank=True)
    url=models.URLField(null=True, blank=True)
    date=models.DateField()
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.resourcename

    class Meta():
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    description=models.CharField(max_length=255)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventtitle

    class Meta():
        db_table='event'
        verbose_name_plural='events'
