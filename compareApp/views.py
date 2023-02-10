from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import datetime
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
    broken = False
    if user.is_authenticated:
        if broken:
            return {"periods": [10,11]}
        # Access the field data of the logged-in user
        Lat = user.homeLat
        Long = user.homeLong
        APIKey= "c769a1059b5e4ce689841344230902"
        response = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key={APIKey}&q={Lat},{Long}&days=8&aqi=no&alerts=no")
        current = response.json()['current']
        forecast = response.json()['forecast']['forecastday']
        #print(current)
        # cheeseresponse = requests.get("https://cheese-api.onrender.com/random").json()
        # print(cheeseresponse)
        return {'Lat':Lat, 'Long': Long, 'current':current, "forecast":forecast, }#"cheese":cheeseresponse}
    else:
        # Return an error message for unauthenticated users
        return {'error': 'Please log in to access the API data.'}
#####    
