from django.db import models




class Equipment(models.Model):
    devicename = models.CharField(max_length=100)
    devicetype = models.CharField(max_length=100)
    quantity = models.IntegerField()
    audit = models.DateField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contactnumber = models.CharField(max_length=100)
    emergencycontact = models.CharField(max_length=100)

class Reservation(models.Model):
    reservationstatus = models.CharField(max_length=100)
    reservationdate = models.DateField()
    returndate = models.DateField()
    isoverdue = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Equipment, on_delete=models.CASCADE)






# Create your models here.
