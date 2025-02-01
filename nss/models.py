from django.db import models
from django.db.models import Sum
from PIL import Image
# Create your models here.
class Department(models.Model):
    dep_id=models.IntegerField(primary_key=True)
    dep_name=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return f"{self.dep_name}"
class Programme(models.Model):
    programme_id=models.IntegerField(primary_key=True)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    program_name=models.CharField(max_length=100)
    no_of_sems=models.IntegerField()
    grad_level=models.CharField(max_length=10)
    def __str__(self):
        return f"{self.program_name}"

class volunteer(models.Model):
    volunteer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    status=models.CharField(default='active',max_length=20)
    guard_name=models.CharField(max_length=25)
    guard_mob_no=models.IntegerField()
    sex_choices=[
        ('male','Male'),('female','Female')
    ]
    sex=models.CharField(max_length=15,choices=sex_choices)
    dob=models.DateField()
    year_choices= [(1, '1'), (2, '2'), (3, '3')]
    year=models.IntegerField(choices=year_choices)
    community_choices=[
        ('ST','ST'),('SC','SC'),('General','General'),('OBC','OBC')
    ]
    community=models.CharField(max_length=15,choices=community_choices)
    address=models.TextField()
    blood_group_choices=[
        ('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')
    ]
    blood_group=models.CharField(max_length=15,choices=blood_group_choices)
    height=models.IntegerField()
    unit_choices=[(4, '4'), (5, '5'), (96, '96')]
    unit=models.IntegerField(choices=unit_choices)
    weight=models.IntegerField()
    mobile_no=models.IntegerField()
    Email_id=models.EmailField()
    year_of_enrollment=models.IntegerField()    
    cultural_talents=models.TextField()
    hobbies=models.TextField()
    roll_no=models.IntegerField(unique=False,null=True)
    image=models.ImageField(upload_to='volunteers',default="")
    program=models.ForeignKey(Programme,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
    def total_hours(self):
        return self.attendances.aggregate(Sum('no_of_hours'))['no_of_hours__sum'] or 0
    
class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=60)
    date=models.DateField()
    def __str__(self):
        return f"{self.event_name}"
class Attendance_status(models.Model):
    status_id=models.AutoField(primary_key=True)
    date=models.DateField()
    unit=models.IntegerField()
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name='eventattendances')
    status=models.CharField(max_length=30,default="pending for approval")
class Attendance(models.Model):
    Attendance_status=models.ForeignKey(Attendance_status,on_delete=models.CASCADE)
    Attendance_id=models.AutoField(primary_key=True)
    volunteer=models.ForeignKey(volunteer,on_delete=models.CASCADE,related_name='attendances')
    date=models.DateField()
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    no_of_hours=models.IntegerField()
    def __str__(self):
        return f"{self.event.event_name}"
class Event_details(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name='eventdetails') 
    des=models.TextField()
    expense=models.TextField(null=True)
    def __str__(self):
        return f"{self.event.event_name}"

class Event_Photos(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE,related_name='eventphotos')
    photo=models.ImageField(upload_to='events')

class Camp(models.Model):
    camp_id=models.AutoField(primary_key=True)
    camp_name=models.CharField(max_length=40,null=True)
    fromdate=models.DateField()
    todate=models.DateField()
    
class Camp_Attendance(models.Model):
    Attendance_id=models.AutoField(primary_key=True)
    volunteer=models.ForeignKey(volunteer,on_delete=models.CASCADE,related_name='camp_attendances')
    camp=models.ForeignKey(Camp,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.camp.camp_name}"

class Camp_event(models.Model):
    event_id=models.AutoField(primary_key=True)
    camp=models.ForeignKey(Camp,on_delete=models.CASCADE)
    event_name=models.CharField(max_length=60)
    des = models.TextField()
    date=models.DateField()
    def __str__(self):
        return f"{self.event_name}"

class Camp_event_photos(models.Model):
    event = models.ForeignKey(Camp_event, on_delete=models.CASCADE, related_name='camp_eventphotos')
    photo = models.ImageField(upload_to='events')
