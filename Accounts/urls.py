from django.urls import path
from . import views

urlpatterns = [
    path('Registeruser/',views.Registeruser,name='Registeruser'),
    path('Registervendor/',views.Registervendor,name='Registervendor'),


]