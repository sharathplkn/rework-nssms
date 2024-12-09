from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(volunteer)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Event)
admin.site.register(Programme)
admin.site.register(Event_details)
admin.site.register(Event_Photos)
admin.site.register(Attendance_status)
admin.site.register(Camp)
admin.site.register(Camp_Attendance)
admin.site.register(Camp_event)
admin.site.register(Camp_event_photos)