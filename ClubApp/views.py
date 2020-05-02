from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ClubInformation, Meeting, MeetingMinute, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'ClubApp/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'ClubApp/resources.html', {'resource_list':resource_list})

def getmeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'ClubApp/meetings.html', {'meeting_list':meeting_list})

def meetingdetails(request, id):
    meetingid = get_object_or_404(Meeting, pk=id)
    meetingMinutes = MeetingMinute.objects.get(meetingid=id)
    attendance = meetingMinutes.attendance.count()
    minutes = meetingMinutes.minutes

    context={
        'meetingid' : meetingid,
        'attendance'  : attendance,
        'minutes' : minutes,
    }
    return render(request, 'ClubApp/meetingdetail.html', context=context)
    