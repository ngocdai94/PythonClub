from django.shortcuts import render
from .models import ClubInformation, Meeting, MeetingMinute, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'ClubApp/index.html')

def getresources(request):
    resource_list=Resource.objects.all()
    return render(request, 'ClubApp/resources.html', {'resource_list':resource_list})