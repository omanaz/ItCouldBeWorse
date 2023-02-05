from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accountHome')

    else:
        form = UserCreationForm()
    return render(request, 'CompareApp/login.html', {'form': form})


def accountHome(request):
    #data = get_data()
    return render(request, 'CompareApp/accountManage.html')

@login_required
def get_data():
    # Your code to retrieve the data you want to return
    data = [1, 2, 3, 4, 5]

    return JsonResponse(data, safe=False)