from django import forms
from .models import Task, Users
from django.contrib.auth.forms import AuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date_time', 'assigned_to']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'email', 'mobile_number', 'address','password']

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(label="password", strip=False, widget=forms.PasswordInput())
