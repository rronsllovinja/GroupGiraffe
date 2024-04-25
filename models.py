from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

class Rental(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  # Default to 1 if not specified
    start_date = models.DateField()
    end_date = models.DateField()

