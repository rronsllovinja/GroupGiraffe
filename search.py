from django.shortcuts import render
from .models import Equipment

def search_results(request):
    if 'item_id' in request.GET:
        item_id = request.GET['item_id']
        # Perform a query to find the item by ID, assuming YourModelName has a field named 'id'
        items = YourModelName.objects.filter(id=item_id)
        context = {'items': items}
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'search_results.html')
