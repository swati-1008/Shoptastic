from django.shortcuts import render

# Create your views here.

def mdfwalldecor(request):
    context = {
        'product_name': 'Santosha Decor MDF Metallic Paint Wall Deocration Shelf Rack, (Red and White) - Set of 6',
        'price': '1,099'
    }
    return render(request, 'Furniture/mdfwalldecor.html', context=context)