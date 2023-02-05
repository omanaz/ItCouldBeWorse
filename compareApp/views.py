from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . import forms

# Create your views here.
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accountHome')
    else:
        form = AuthenticationForm()
    return render(request, 'CompareApp/login.html', {'form': form})

from django.contrib.auth import login
from . import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView
from compareApp.models import User

class register(CreateView):
    model = User
    form_class = forms.fullUser
    template_name = 'CompareApp/login.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        login(self.request, user)
        return response


def accountHome(request):
    #data = get_data()
    return render(request, 'CompareApp/accountManage.html')

@login_required
def get_data():
    # Your code to retrieve the data you want to return
    data = [1, 2, 3, 4, 5]

    return JsonResponse(data, safe=False)