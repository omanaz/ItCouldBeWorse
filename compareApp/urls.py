from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('Home/', views.accountHome, name='accountHome'),
    path('accountCreation/', views.register.as_view(), name='register'),
    path('get_data/', views.get_data, name='get_data'),
]