from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ClubInformation, Meeting, MeetingMinute, Resource, Event

# Create your tests here.             
##----------------------------- TESTING MODELS ------------------------------##
class ClubInformationTest(TestCase):
   def test_string(self):
      type=ClubInformation(clubname='Python Club Test')
      self.assertEqual(str(type), type.clubname)

   def test_table(self):
      self.assertEqual(str(ClubInformation._meta.db_table), 'clubinformation')

class MeetingTest(TestCase):  
   def setup(self):
      meeting=Meeting(
         meetingtitle='Python Meeting', 
         meetingdate='2020-01-05', 
         meetingtime='10:00', 
         meetinglocation='Seattle', 
         meetingagenda='https://drive.google.com/agendalink')
      return meeting

   def test_string(self):
      meeting=self.setup()
      self.assertEqual(str(meeting), meeting.meetingtitle)

   def test_table(self):
      self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinuteTest(TestCase):
   def test_string(self):
      type=MeetingMinute(minutes='90')
      self.assertEqual(str(type), type.minutes)

   def test_table(self):
      self.assertEqual(str(MeetingMinute._meta.db_table), 'meetingminute')

class ResourceTest(TestCase):
   def setup(self):
      resource=Resource(
         resourcename='Python Books', 
         resourcetype='online', 
         url='https://pythonbooks.org/free-books/', 
         date='2020-01-05', 
        #    userid='',
         description='Python for everyone')
      return resource

   def test_string(self):
      resource = self.setup()
      self.assertEqual(str(resource), resource.resourcename)
    
   def test_type(self):
      resource=self.setup()
      self.assertEqual(str(resource.resourcetype), 'online')

   def test_table(self):
      self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
   def setup(self):
      event=Event(
         eventtitle='Python Hiring', 
         location='Seattle', 
         date='2020-01-05', 
         time='10:00', 
         description='Seeking Python Developer',
         #userid
      )
      return event

   def test_string(self):
      event = self.setup()
      self.assertEqual(str(event), event.eventtitle)

   def test_table(self):
      self.assertEqual(str(Event._meta.db_table), 'event')
##---------------------------- TESTING MODELS ENDS --------------------------##

##----------------------------- TESTING VIEWS ------------------------------##
## Sample Data
class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('index'))
      self.assertEqual(response.status_code, 200)

class GetResourcesTest(TestCase):
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('resources'))
      self.assertEqual(response.status_code, 200)

class GetMeetingTest(TestCase):
   def test_view_url_accessible_by_name(self):
      response = self.client.get(reverse('meetings'))
      self.assertEqual(response.status_code, 200)

class GetMeetingDetailTest(TestCase):
   def setUp(self):
      self.u=User.objects.create(username='myuser')
      self.meeting=Meeting.objects.create(meetingtitle="Python Meeting",
                                          meetingdate='2020-05-06',
                                          meetingtime='9:00',
                                          meetinglocation='Seattle',
                                          meetingagenda='https://drive.google.com/agendalink')
      self.meetingMin1=MeetingMinute.objects.create(meetingid=self.meeting, minutes='90')
      self.meetingMin1.attendance.add(self.u)

   def test_meeting_detail_success(self):
      response = self.client.get(reverse('meetingdetails', args=(self.meeting.id,)))
      # Assert that self.post is actually returned by the post_detail view
      self.assertEqual(response.status_code, 200)