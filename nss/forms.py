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
