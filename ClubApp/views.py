from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import ResourceForm, MeetingForm
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
    return render(request, 'ClubApp/meetingdetails.html', context=context)
    
def newResource(request):
    form=ResourceForm
    if request.method=="POST":
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
        else:
            form=ResourceForm()
    return render(request, 'ClubApp/newresource.html', {'form':form})

def newMeeting(request):
    form=MeetingForm
    if request.method=="POST":
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
        else:
            form=MeetingForm()
    return render(request, 'ClubApp/newmeeting.html', {'form':form})