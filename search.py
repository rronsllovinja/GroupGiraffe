from django.db.models import Q

def home(request):
    
    
    itemtypes = ItemType.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    item = Item.objects.filter
    (Q(itemtype__type__icontains=q)) | 
    (Q(name__icontains=q)) | 
    (Q(itemmaker__maker_icontains=q)) | 
    (Q(ram_icontains=q))

    

    context = {'item':item, 'itemtypes':itemtypes}