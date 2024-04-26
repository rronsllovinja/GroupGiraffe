from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_rented_equipment, name='view_rented_equipment'),
    path('eqiupmentlist', views.equipmentlist),
    path('add_equipment/', views.add_equipment, name = "app/add_equipment.html")
]
