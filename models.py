from django.db import models




class Equipment(models.Model):
    devicename = models.CharField(max_length=100)
    devicetype = models.CharField(max_length=100)
    quantity = models.IntegerField()
    audit = models.DateField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

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

class Equipment(models.Model):
    deviceid = models.IntegerField()
    deviceName = models.CharField(max_length=100)
    deviceType = models.CharField(max_length=100)
    quantity = models.IntegerField()
    audit = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True, default=None)
    comments = models.TextField(blank=True)

    level_categories = [
        ('technology', 'Technology'),
        ('gaming', 'Gaming'),
        ('office', 'Office'),
        ('other', 'Other'),
    ]
    categories = models.CharField(max_length=20, choices=level_categories, default='technology')

    level_availability = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    availability = models.CharField(max_length=20, choices=level_availability, default='available')

    def __str__(self):
        return self.deviceName




# Create your models here.
