from django.shortcuts import render

# Create your views here.

def mdfwalldecor(request):
    context = {
        'product_name': 'Santosha Decor MDF Metallic Paint Wall Deocration Shelf Rack, (Red and White) - Set of 6',
        'price': '1,099'
    }
    return render(request, 'Furniture/mdfwalldecor.html', context=context)

def furniturecafestool(request):
    context = {
        'product_name': 'Furniture Cafe Wooden Stool Sitting Table Natural Wood Logs Smooth Finish Best Used as Bedside Tea Coffee Plants Table for Bedroom Living Room Outdoor Garden Furniture (Round, 16 inches)',
        'price': '1,519'
    }
    return render(request, 'Furniture/furniturecafestool.html', context=context)

def woodkeyholder(request):
    context = {
        'product_name': 'A10 Shop Omega 6 Engineered Wood Key Holder with Wall Decor Shelf, 5 Key Hooks - Mahogany Finish',
        'price': '645'
    }
    return render(request, 'Furniture/a10keyholder.html', context=context)

def storagecase(request):
    context = {
        'product_name': 'Desire Hub 4 Pcs Wall Mounted Storage Case for Remote, Toothbrush , Remote Control Storage Organizer Case for Air Conditioner TV Mobile Phone, Toothbrush, Plug Holder Stand Rack (4)',
        'price': '295'
    }
    return render(request, 'Furniture/storagecase.html', context=context)

def wallmirror(request):
    context = {
        'product_name': 'Hosley Decorative Round Iron Wall Mirror (20.32 cm x 30.48 cm, Black, Set of 2) (G14601)',
        'price': '709'
    }
    return render(request, 'Furniture/wallmirror.html', context=context)

def entunit(request):
    context = {
        'product_name': 'UniArt Wall Mounted TV Entertainment Unit – Perfect for Living Room/Home Décor (White Color)',
        'price': '899'
    }
    return render(request, 'Furniture/tventunit.html', context=context)