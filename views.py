from django.shortcuts import render, redirect
from .models import Equipment, Rental
from .forms import EquipmentForm, RentalForm
from django.db.models import Sum, F
from datetime import date, timedelta
from django.db.models import Count
from django.db.models.functions import Coalesce
from .models import Equipment
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EquipmentForm


def view_rented_equipment(request):
    total_equipment = Equipment.objects.aggregate(total=Sum('quantity'))['total']
    available_equipment = Equipment.objects.all()
    # Find the current date and start of the week
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())  # Monday

    # Calculate the availability for each day of the week
    availability = {}
    for i in range(7):  # 0-6 for Monday to Sunday
        day = start_of_week + timedelta(days=i)
        
        # Count the total quantity of equipment rented out for each day
        rented_out_quantity = Rental.objects.filter(
            start_date__lte=day, 
            end_date__gte=day
        ).aggregate(
            total_rented=Coalesce(Sum('quantity'), 0)
        )['total_rented']
        
        # Subtract the rented out quantity from the total equipment to get availability
        availability[day.strftime('%a').lower()] = total_equipment - rented_out_quantity

    if request.method == 'POST':
        equipment_form  = EquipmentForm(request.POST)
        rental_form = RentalForm(request.POST)
        if equipment_form.is_valid():
            equipment_form.save()
            return redirect('view_rented_equipment')  # Redirect to view rented equipment page
        if rental_form.is_valid():
            equipment_id = rental_form.cleaned_data['equipment'].id  # Extract the primary key
            quantity = rental_form.cleaned_data['quantity']
            start_date = rental_form.cleaned_data['start_date']
            end_date = rental_form.cleaned_data['end_date']
            equipment = Equipment.objects.get(pk=equipment_id)
            if equipment.quantity >= quantity:
                Rental.objects.create(equipment=equipment, quantity=quantity, start_date=start_date, end_date=end_date)
                for i in range(7):  # 0-6 for Monday to Sunday
                    day = start_of_week + timedelta(days=i)
                    
                    # Count the total quantity of equipment rented out for each day
                    rented_out_quantity = Rental.objects.filter(
                        start_date__lte=day, 
                        end_date__gte=day
                    ).aggregate(
                        total_rented=Coalesce(Sum('quantity'), 0)
                    )['total_rented']
                    
                    # Subtract the rented out quantity from the total equipment to get availability
                    availability[day.strftime('%a').lower()] = total_equipment - rented_out_quantity
                return redirect('view_rented_equipment') 
            else:
                # Handle case where requested quantity exceeds available quantity
                error_message = "Requested quantity exceeds available quantity."
                available_equipment = Equipment.objects.all()
                return redirect('view_rented_equipment') 
             
    else:
        rental_form = RentalForm()
        equipment_form = EquipmentForm()

    
    context = {
        'rented_equipment': Rental.objects.all(),
        'total_equipment': total_equipment,
        'availability': availability,
        'equipment_form': equipment_form,
        'rental_form': rental_form,
        "available_equipment":available_equipment
    }
    return render(request, 'view_rented_equipment.html', context)

def test(request):
    return render(request, 'test.html')

def equipmentlist(request):
    equipmentlist = Equipment.objects.all()
    
    return render(request, 'app/equipmentlist.html', {'equipment_list': equipmentlist})
    
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'app/add_equipment.html', {'form': form})
