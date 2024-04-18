from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_rented_equipment, name='view_rented_equipment'),
]
