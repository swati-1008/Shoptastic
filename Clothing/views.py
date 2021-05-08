from django.shortcuts import render

# Create your views here.

def zeellehenga(request):
    context = {
        'product_name': "Zeel Clothing Women's Organza Semi-stitched Lehenga Choli",
        'price': '3,349'
    }
    return render(request, 'Clothing/zeellehenga.html', context=context)

def babyjumpsuit(request):
    context = {
        'product_name': 'TASLAR Unisex Baby Flannel Jumpsuit Panda Style Cosplay Clothes Bunting Outfits Snowsuit Hooded Romper Outwear (Black & White Panda)',
        'price': '1,349'
    }
    return render(request, 'Clothing/babyjumpsuit.html', context=context)

def mensweatshirt(request):
    context = {
        'product_name': "LEWEL Men's Cotton Hooded Sweatshirt",
        'price': '469'
    }
    return render(request, 'Clothing/mensweatshirt.html', context=context)

def menshirt(request):
    context = {
        'product_name': "FINIVO FASHION Men's Cotton Casual Shirt",
        'price': '687'
    }
    return render(request, 'Clothing/menshirt.html', context=context)

def babyromper(request):
    context = {
        'product_name': 'Popees Short Sleeve T-Shirt with Romper for Baby Boys & Girls (Large - 12-18 Months)',
        'price': '435'
    }
    return render(request, 'Clothing/babyromper.html', context=context)

def bandhejsaree(request):
    context = {
        'product_name': "Cloth Clock Women's Bandhani Bandhej Khadi Silk Saree With Blouse Piece (Free Size_Multi Color)",
        'price': '399'
    }
    return render(request, 'Clothing/bandhejsaree.html', context=context)