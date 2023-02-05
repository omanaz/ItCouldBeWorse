from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['homeLong',"homeLat"]


class fullUser(UserCreationForm):
    #homeLong = forms.FloatField()
    #homeLat = forms.FloatField()
    #profilePicture = forms.ImageField()

    class Meta:
        model = models.User
        fields = ['username', 'password1', 'password2']
