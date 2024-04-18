from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipment

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def blist(request):
    return render(request, 'app/blist.html')

def navbar (request):
        return render(request, 'navbar.html')

def searchforequipment (request):
       return render(request, 'app/searchforeqiupment.html')

def equipmentlist(request):
    equipmentlist = Equipment.objects.all()
    
    return render(request, 'app/equipmentlist.html', {'equipment_list': equipmentlist})

def profile(request):
    user = request.user
    return render(request, 'app/profile.html', {'user': user})

def beginner(request):
      return render(request, 'app/beginner.html')

def intermediate(request):
      return render(request,'app/intermediate.html') 

def professional(request):
      return render(request,'app/professional.html')  


def beginner_devices(request):
    beginner_devices = Equipment.objects.filter(level='beginner')
    return render(request, 'beginner.html', {'beginner_devices': beginner_devices})
from django.shortcuts import render
from .models import Equipment

def equipment_list_view(request):
    equipment_list = Equipment.objects.all()  # Query all equipment items
    return render(request, 'equipmentlist.html', {'equipment_list': equipment_list})



