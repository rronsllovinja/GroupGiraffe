from django.db import models

# Create your models here.
class Equipment(models.Model):
    deviceid = models.IntegerField()
    deviceName = models.CharField(max_length=100)
    deviceType = models.CharField(max_length=100)
    quantity = models.IntegerField()
    audit = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True,default=None)
    comments = models.TextField(blank=True)

    level_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('professional', 'Professional'),
    ]
    level = models.CharField(max_length=20, choices=level_choices, default='beginner')

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