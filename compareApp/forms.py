from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.safestring import mark_safe

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['homeLong',"homeLat"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True, "autocomplete": 'off', 'id': "username"}),
        label=mark_safe('Username<br>:::'),
        help_text=':::'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": 'off'}),
        label=mark_safe('Password<br>:::'),
        help_text=':::'
    )


class fullUser(UserCreationForm):
    #homeLong = forms.FloatField()
    #homeLat = forms.FloatField()
    #profilePicture = forms.ImageField()
    class Meta:
        model = models.User
        fields = ['username', 'password1', 'password2']
        
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True, "autocomplete": 'off', 'id': "username"}),
        label=mark_safe('Username'),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": 'off'}),
        label=mark_safe('Password'),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": 'off'}),
        label=mark_safe('Password'),
        help_text=mark_safe("<br>(Confirm)")
    )
