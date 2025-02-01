from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Group,Permission
from .models import volunteer, Event, Event_details, Event_Photos, Camp, Camp_event, Camp_event_photos, Programme

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

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = volunteer
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = Event_details
        fields = ['des', 'expense']

class EventPhotosForm(forms.ModelForm):
    class Meta:
        model = Event_Photos
        fields = ['photo', 'event']

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ['camp_name', 'fromdate', 'todate']
        widgets = {
            'fromdate': forms.DateInput(attrs={'type': 'date'}),
            'todate': forms.DateInput(attrs={'type': 'date'}),
        }

class CampEventForm(forms.ModelForm):
    class Meta:
        model = Camp_event
        fields = ['camp', 'event_name', 'des', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CampEventPhotosForm(forms.ModelForm):
    class Meta:
        model = Camp_event_photos
        fields = ['photo', 'event']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'groups']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'groups']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']