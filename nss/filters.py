import django_filters
from django_filters import *
from .models import volunteer  # Adjust import based on your actual model name

class VolunteerFilter(django_filters.FilterSet):
    year_of_enrollment=CharFilter(field_name='year_of_enrollment',lookup_expr='icontains')
    name=CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = volunteer
        exclude = ['image','status','guard_name','guard_mob_no','dob','address','height','weight','mobile_no','Email_id','cultural_talents','hobbies','roll_no']
class VolunteerFilter2(django_filters.FilterSet):
    year_of_enrollment=CharFilter(field_name='year_of_enrollment',lookup_expr='icontains')
    name=CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = volunteer
        exclude = ['blood_group','community','image','status','guard_name','guard_mob_no','dob','address','height','weight','mobile_no','Email_id','cultural_talents','hobbies','roll_no']
