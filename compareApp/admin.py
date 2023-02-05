from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'homeLong', 'homeLat', 'profilePicture')


admin.site.register(User, UserAdmin)