from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('Home/', views.accountHome, name='accountHome'),
    path('accountCreation/', views.register.as_view(), name='register'),
    path('getData/', views.getEarthData, name='getData'),
    path('EarthWeather/', views.earthView, name="earthView"),
    path('Mars/', views.marsView, name="mars"),
    path('commerce/', views.commerce_view,name='commerce')
]