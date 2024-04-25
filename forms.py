# forms.py
from django import forms
from .models import Equipment, Rental

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'category', 'quantity']

class RentalForm(forms.ModelForm):
    start_date = forms.DateField(input_formats=['%Y-%m-%d'])
    end_date = forms.DateField(input_formats=['%Y-%m-%d'])
    quantity = forms.IntegerField(min_value=1)  # Add this line
    class Meta:
        model = Rental
        fields = ['equipment', 'quantity', 'start_date', 'end_date']  # Include 'quantity'

