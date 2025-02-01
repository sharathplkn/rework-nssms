from django import forms
from django.contrib.auth.models import User, Group, Permission
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'password', 'email', 'is_active', 'groups',
        ]
        widgets = {
            'password': forms.PasswordInput(),  # Secure password input
        }

    def save(self, commit=True):
        user = super().save(commit=False)  # Use super() without parameters
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            self.save_m2m()
        return user

class UserForm3(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.filter(name='vs'))

    class Meta:
        model = User
        fields = [
            'username', 'password', 'email', 'is_active', 'groups',
        ]
        widgets = {
            'password': forms.PasswordInput(),  # Secure password input
        }

    def save(self, commit=True):
        user = super().save(commit=False)  # Correctly reference UserForm3
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            self.save_m2m()
        return user

class UserForm2(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'groups']

class UserForm4(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.filter(name='vs'))

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'groups']

class GroupForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']



class addVolunteerForm(forms.ModelForm):
    class Meta:
        model = volunteer
        fields = [
            'name', 'guard_name', 'guard_mob_no', 'sex', 'dob', 'program', 'year',
            'community', 'address', 'blood_group', 'height', 'weight', 'mobile_no',
            'Email_id', 'year_of_enrollment', 'cultural_talents', 'hobbies', 'roll_no',
            'image', 'unit'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'program': forms.Select(),
        }

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date']
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = Event_details
        fields = ['des', 'expense']
        widgets = {
            'des': forms.Textarea(attrs={'class': 'form-control'}),
            'expense': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EventPhotosForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Event_Photos
        fields = ['photo']

class DepartmentWiseForm(forms.Form):
    UNIT_CHOICES = [
        ('', 'Select Unit'),  # Added empty choice
        ('4', 'Unit 4'),
        ('5', 'Unit 5'),
        ('96', 'Unit 96'),
    ]
    
    unit = forms.ChoiceField(
        choices=UNIT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True
        })
    )
    
    event = forms.ModelChoiceField(
        queryset=Event.objects.all().order_by('-date'),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True
        }),
        empty_label="Select event"
    )

class AttendanceForm(forms.Form):
    UNIT_CHOICES = [
        ('', 'Select Unit'),  # Added empty choice
        ('4', 'Unit 4'),
        ('5', 'Unit 5'),
        ('96', 'Unit 96'),
    ]
    
    event = forms.ModelChoiceField(
        queryset=Event.objects.all().order_by('-date'),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True
        }),
        empty_label="Select event"
    )
    
    unit = forms.ChoiceField(
        choices=UNIT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True
        })
    )

class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date']
        widgets = {
            'event_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': True
            })
        }

class EditEventDetailsForm(forms.ModelForm):
    class Meta:
        model = Event_details
        fields = ['des']
        widgets = {
            'des': forms.Textarea(attrs={
                'class': 'form-control',
                'required': True
            })
        }

class MonthlyReportForm(forms.Form):
    MONTH_CHOICES = [
        ('', 'Select Month'),
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]
    
    YEAR_CHOICES = [(str(year), str(year)) for year in range(2020, 2031)]
    YEAR_CHOICES.insert(0, ('', 'Select Year'))
    
    month = forms.ChoiceField(
        choices=MONTH_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True,
            'style': 'display: block; width: 100%;'
        })
    )
    
    year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True,
            'style': 'display: block; width: 100%;'
        })
    )

class YearlyReportForm(forms.Form):
    fromyear = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'required': True,
            'style': 'display: block; width: 100%;'
        })
    )
    
    toyear = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'required': True,
            'style': 'display: block; width: 100%;'
        })
    )

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ['camp_name', 'fromdate', 'todate']
        widgets = {
            'camp_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Enter Camp Name'
            }),
            'fromdate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': True
            }),
            'todate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': True
            })
        }

class CampEventForm(forms.ModelForm):
    class Meta:
        model = Camp_event
        fields = ['event_name', 'date', 'des', 'camp']
        widgets = {
            'event_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Enter Event Name'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': True
            }),
            'des': forms.Textarea(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Enter Description'
            }),
            'camp': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            })
        }

class CampPhotoForm(forms.ModelForm):
    class Meta:
        model = Camp_event_photos
        fields = ['photo']
        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'required': True,
                'accept': 'image/*'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'] = forms.ModelChoiceField(
            queryset=Camp_event.objects.all().order_by('-date'),
            widget=forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            empty_label="Select event"
        )

class EditCampEventForm(forms.ModelForm):
    class Meta:
        model = Camp_event
        fields = ['event_name', 'date', 'des', 'camp']
        widgets = {
            'event_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'required': True
            }),
            'des': forms.Textarea(attrs={
                'class': 'form-control',
                'required': True
            }),
            'camp': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            })
        }

class UnitWiseAttendanceForm(forms.Form):
    UNIT_CHOICES = [
        ('', 'Select Unit'),
        ('4', 'Unit 4'),
        ('5', 'Unit 5'),
        ('96', 'Unit 96'),
    ]
    
    unit = forms.ChoiceField(
        choices=UNIT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'required': True
        })
    )
    
    from_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'required': True
        })
    )
    
    to_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'required': True
        })
    )
