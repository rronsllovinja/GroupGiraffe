from django import forms
from .models import Equipment

class CreateInventoryForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        
class EquipmentSearchForm(forms.Form):
    query = forms.CharField(label='Search for equipment', max_length=100)

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['deviceName', 'deviceType', 'quantity', 'availability']


