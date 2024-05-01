from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Equipment
from .forms import CreateInventoryForm, EquipmentSearchForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import EquipmentForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
def login_page(request):
    return render(request, 'app/login.html')

def logout_page(request):
    return render(request, 'app/logout.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('homepage')
    else:
            form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'app/home.html')


def notification (request):
        return render(request, 'app/notification.html')

def notification_page(request):
    return render(request, 'app/notification_page.html')

def searchforequipment (request):
       return render(request, 'app/searchforeqiupment.html')

def equipmentlist(request):
    query = request.GET.get('q', '')
    device_id = request.GET.get('device_id', '')
    equipmentlist = Equipment.objects.all()

    if device_id:
        equipmentlist = equipmentlist.filter(deviceid=device_id)
    
    return render(request, 'app/equipmentlist.html', {'equipment_list': equipmentlist})

def profile(request):
    user = request.user
    return render(request, 'app/profile.html', {'user': user}) 


def equipment_detail(request, equipment_id):
    equipment = get_object_or_404(Equipment, pk=equipment_id)
    return render(request, 'equipment_detail.html', {'equipment': equipment})


def CreateInventory(request):
    if request.method == "POST":
        form = CreateInventoryForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect(reverse('equipmentlist'))  # Corrected URL pattern name
    else:
        form = CreateInventoryForm()
    return render(request, "app/createinventory.html", {"form": form})

def equipment_search(request):
    form = EquipmentSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Equipment.objects.filter(deviceName__icontains=query)
    else:
        results = Equipment.objects.none()
    return render(request, 'equipment_search.html', {'form': form, 'results': results})

def update_equipment(request, device_id):
    equipment = Equipment.objects.get(deviceid=device_id)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipmentlist')  # Redirect to equipment list page after update
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'app/update_equipment.html', {'form': form})

def deleteItem(request, device_id):
    equipment = Equipment.objects.get(deviceid=device_id)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipmentlist')
    return render(request, 'app/deleteitem.html', {'equipment': equipment})

def create_item_view(request):
    if request.method == "POST":
        form = CreateInventoryForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect(reverse('equipmentlist'))  # Corrected URL pattern name
    else:
        form = CreateInventoryForm()
    return render(request, "app/createinventory.html", {"form": form})


def view_rented_equipment(request):

    return render(request, 'app/view_rented_equipment.html')





def reservation_page(request):
    return render(request, 'app/reservation_page.html')

def notification_page(request):
    return render(request, 'app/notification_page.html')  # Correct template name



def save_notification_settings(request):
    if request.method == 'POST':
        email_notifications = request.POST.get('emailNotifications', False)
        sms_notifications = request.POST.get('smsNotifications', False)
        push_notifications = request.POST.get('pushNotifications', False)
        
        # Process the notification settings here (e.g., update user preferences in the database)
        
        # Assuming the user is redirected to the profile page after saving
        # You can customize the success message as needed
        messages.success(request, 'Notification settings saved successfully')  # Customize success message
        return redirect('profile')  # Redirect to profile page after saving
    else:
        return HttpResponse('Invalid method')  # Handle invalid method gracefully
