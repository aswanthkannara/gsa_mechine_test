import requests
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import *
from .models import Users, Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data= request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            print(email)
            password = form.cleaned_data.get('password')
            print(password)
            if Users.objects.filter(email=email,password=password).exists():
                # if user is not None:
                # login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'loginPage.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('aa')
            user_profile = form.save(commit=False)
            address = form.cleaned_data.get('address')
            api_key = settings.GOOGLE_MAPS_API_KEY
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
            
            response = requests.get(url)
            data = response.json()
            print('g data  --0',data)
            
            # if data['status'] == 'OK':
            #     result = data['results'][0]
            #     user_profile.latitude = result['geometry']['location']['lat']
            #     user_profile.longitude = result['geometry']['location']['lng']
            
            user_profile.save()
            return redirect('/')
            # return render(request, 'registration_success.html', {'user_profile': user_profile})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def dashboard(request):
    return render(request,'dashboard.html')

def add_task_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        task = Task.objects.create(
            name=data.get('task_name'),
            date_time=data.get('task_datetime'),
            assigned_to_id=data.get('task_assignee')
        )
        print('999',task.assigned_to)
        return JsonResponse({'task': {
            'name': task.name,
            'datetime': task.date_time,
            'assignee': task.assigned_to.email
        }})
    else:
        pass
