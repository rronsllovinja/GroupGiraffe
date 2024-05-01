from django.contrib import admin

# Register your models here.
from .models import Equipment, Rental,Reservation,User

admin.site.register(Equipment)
admin.site.register(Reservation)
admin.site.register(Rental)
admin.site.register(User)