from django.shortcuts import render

# Create your views here.

def oneplus(request):
    context = {
        'price': '59,999',
        'color': 'Ultramarine Blue',
        'product_name': 'One Plus 8 Pro',
        'product_specs': '12 GB Ram + 256 GB Storage'
    }
    return render(request, 'Mobiles/onepluseightpro.html', context=context)

def redmi9power(request):
    context = {
        'price': '10,499',
        'color': 'Blazing Blue',
        'product_name': 'Redmi 9 Power',
        'product_specs': '4 GB RAM + 64 GB Storage'
    }
    return render(request, 'Mobiles/redmi9power.html', context=context)

def samsunggalaxym51(request):
    context = {
        'price': '22,999',
        'color': 'Electric Blue',
        'product_name': 'Samsung Galaxy M51',
        'product_specs': '6 GB RAM + 128 GB Storage'
    }
    return render(request, 'Mobiles/samsunggalaxym51.html', context=context)

def iphone12mini(request):
    context = {
        'price': '69,900',
        'color': 'Blue',
        'product_name': 'IPhone 12 Mini',
        'product_specs': '64 GB'
    }
    return render(request, 'Mobiles/iphone12mini.html', context=context)

def nokia34(request):
    context = {
        'price': '11,999',
        'color': 'Fjord',
        'product_name': 'Nokia 3.4',
        'product_specs': '4 GB RAM + 64 GB Storage'
    }
    return render(request, 'Mobiles/nokia3.4.html', context=context)

def vivoy20(request):
    context = {
        'price': '12,990',
        'color': 'Purist Blue',
        'product_name': 'Vivo Y20',
        'product_specs': '4 GB RAM + 64 GB Storage'
    }
    return render(request, 'Mobiles/vivoy20.html', context=context)