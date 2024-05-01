from django.db import models

class Equipment(models.Model):
    deviceid = models.IntegerField()
    deviceName = models.CharField(max_length=100)
    deviceType = models.CharField(max_length=100)
    quantity = models.IntegerField()
    audit = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True, default=None)
    comments = models.TextField(blank=True)
    reservation = models.ForeignKey('Reservation', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipment_reservations')
    user = models.ForeignKey('User',on_delete=models.SET_NULL, null=True, blank=True, related_name='equipment_users')

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
    
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Reservation(models.Model):
    reservationstatus = models.CharField(max_length=100)
    reservationdate = models.DateField()
    returndate = models.DateField()
    isoverdue = models.BooleanField()
    device = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='reservations')

    def __str__(self):
        return f"{self.device.deviceName} - {self.reservationstatus}"
    
class Rental(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  # Default to 1 if not specified
    start_date = models.DateField()
    end_date = models.DateField()