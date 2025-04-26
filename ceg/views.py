from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import SignUpForm, CustomLoginForm
import requests

THINGSPEAK_CHANNEL_ID = '2756474'
READ_API_KEY = '3XGCUU9NH3ATULEB'

def get_thingspeak_data():
    url = f'https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds.json?results=2'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def db(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = get_thingspeak_data()
    if data:
        feeds = data['feeds']
        voltage_data = [feed['field2'] for feed in feeds if feed['field2'] is not None]
        current_data = [feed['field3'] for feed in feeds if feed['field3'] is not None]
        return render(request, 'dashboard.html', {
            'voltage_data': voltage_data,
            'current_data': current_data
        })
    return render(request, 'dashboard.html', {})  # Fallback if no data

def login(request):
    if request.user.is_authenticated:
        return redirect('Watertracking')

    signup_form = SignUpForm()
    login_form = CustomLoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        # Handle login
        if 'login' in request.POST:
            login_form = CustomLoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user)
                return redirect('Watertracking')
            else:
                messages.error(request, "Invalid login credentials.")

        # Handle signup
        elif 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, "Account created successfully! Please log in.")
                return redirect('login')
            else:
                messages.error(request, "Signup failed. Please correct the errors below.")

    return render(request, 'login.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })

def logout(request):
    auth_logout(request)
    return redirect('login')

def tab(request):
    return render(request, 'tables.html')

def noti(request):
    return render(request, 'notifications.html')

def watertracking(request):
    return render(request, 'Watertracking.html')

def profile1(request):
    return render(request, 'profile1.html')

def waterbilling(request):
    return render(request, 'waterbilling.html')
