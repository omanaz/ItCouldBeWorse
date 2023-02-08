from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from compareApp.models import User


# User: Login Register Change data Views
def loginView(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('earthView')
    else:
        form = forms.LoginForm()
    return render(request, 'compareApp/login.html', {'form': form, 'formname': 'login'})
class register(CreateView):
    model = User
    form_class = forms.fullUser
    template_name = 'CompareApp/login.html'
    success_url = reverse_lazy('earthView')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        login(self.request, user)
        return response
from django.shortcuts import render, redirect
from .forms import UserUpdateForm

def accountHome(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accountHome')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'compareApp/accountManage.html', {'form': form, 'showbanner':True})




#####

#Simple Page Views
#def accountHome(request):
    #data = get_data()
    #return render(request, 'CompareApp/accountManage.html')
def earthView(request):
    data = getData(request)
    return render(request, 'compareApp/landingPage.html', {'data':data, 'showbanner':True})
#####    


### API Views
import requests
@login_required
def getData(request):
    user = request.user
    broken = True
    if user.is_authenticated:
        if broken:
            return {"periods": [10,11]}
        # Access the field data of the logged-in user
        Lat = user.homeLat
        Long = user.homeLong
        response = requests.get(f"https://api.weather.gov/points/{Lat},{Long}")
        properties = response.json()["properties"]
        # Get the forecast URL from the properties object
        forecast_url = properties["forecast"]
        # Get the hour-by-hour forecast URL from the properties object
        forecast_hourly_url = properties["forecastHourly"]
        # Get the forecast data from the forecast URL
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()
        # Get the hour-by-hour forecast data from the forecastHourly URL
        forecast_hourly_response = requests.get(forecast_hourly_url)
        forecast_hourly_data = forecast_hourly_response.json()
        periods = forecast_data["properties"]["periods"]
        #for i in periods:
         #   print(i)
          #  print('------------------------------------------------------')
        #print(periods)
        return {'periods':periods}
    
        data = response.json()
        return data
    else:
        # Return an error message for unauthenticated users
        return {'error': 'Please log in to access the API data.'}
#####    
