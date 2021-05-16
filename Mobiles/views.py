from django.shortcuts import render
from .models import *

# Create your views here.

def oneplus(request):
    # row = Mobiles.objects.get(product_id='MOB1')
    # print(row.product_name)
    # features = list(Features.objects.filter(pid=row))
    # for i in features:
    #     print(i.features)
    row = Mobiles.objects.get(product_id='MOB1')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/mobiles/onepluseightpro/' + str(row.image1),
        'image2': '../static/images/mobiles/onepluseightpro/' + str(row.image2),
        'image3': '../static/images/mobiles/onepluseightpro/' + str(row.image3),
        'image4': '../static/images/mobiles/onepluseightpro/' + str(row.image4),
        'image5': '../static/images/mobiles/onepluseightpro/' + str(row.image5),
        'os': row.os,
        'ram': row.ram,
        'product_dimensions': row.product_dimensions,
        'batteries': row.batteries,
        'item_model_number': row.item_model_number,
        'wireless': row.wireless,
        'special': row.special,
        'display': row.display,
        'camera': row.camera,
        'form_factor': row.form_factor,
        'battery_power': row.battery_power,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'manufacture_address': row.manufacture_address,
        'generic_name': row.generic_name,
        'features': features
    }
    return render(request, 'Mobiles/onepluseightpro.html', context=context)

def redmi9power(request):
    row = Mobiles.objects.get(product_id='MOB2')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/mobiles/redmi9power/' + str(row.image1),
        'image2': '../static/images/mobiles/redmi9power/' + str(row.image2),
        'image3': '../static/images/mobiles/redmi9power/' + str(row.image3),
        'image4': '../static/images/mobiles/redmi9power/' + str(row.image4),
        'image5': '../static/images/mobiles/redmi9power/' + str(row.image5),
        'os': row.os,
        'ram': row.ram,
        'product_dimensions': row.product_dimensions,
        'batteries': row.batteries,
        'item_model_number': row.item_model_number,
        'wireless': row.wireless,
        'special': row.special,
        'display': row.display,
        'camera': row.camera,
        'form_factor': row.form_factor,
        'battery_power': row.battery_power,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'manufacture_address': row.manufacture_address,
        'generic_name': row.generic_name,
        'features': features
    }
    return render(request, 'Mobiles/redmi9power.html', context=context)

def samsunggalaxym51(request):
    row = Mobiles.objects.get(product_id='MOB3')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/mobiles/onepluseightpro/' + str(row.image1),
        'image2': '../static/images/mobiles/onepluseightpro/' + str(row.image2),
        'image3': '../static/images/mobiles/onepluseightpro/' + str(row.image3),
        'image4': '../static/images/mobiles/onepluseightpro/' + str(row.image4),
        'image5': '../static/images/mobiles/onepluseightpro/' + str(row.image5),
        'os': row.os,
        'ram': row.ram,
        'product_dimensions': row.product_dimensions,
        'batteries': row.batteries,
        'item_model_number': row.item_model_number,
        'wireless': row.wireless,
        'special': row.special,
        'display': row.display,
        'camera': row.camera,
        'form_factor': row.form_factor,
        'battery_power': row.battery_power,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'manufacture_address': row.manufacture_address,
        'generic_name': row.generic_name,
        'features': features
    }
    return render(request, 'Mobiles/samsunggalaxym51.html', context=context)

def iphone12mini(request):
    row = Mobiles.objects.get(product_id='MOB6')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/mobiles/onepluseightpro/' + str(row.image1),
        'image2': '../static/images/mobiles/onepluseightpro/' + str(row.image2),
        'image3': '../static/images/mobiles/onepluseightpro/' + str(row.image3),
        'image4': '../static/images/mobiles/onepluseightpro/' + str(row.image4),
        'image5': '../static/images/mobiles/onepluseightpro/' + str(row.image5),
        'os': row.os,
        'ram': row.ram,
        'product_dimensions': row.product_dimensions,
        'batteries': row.batteries,
        'item_model_number': row.item_model_number,
        'wireless': row.wireless,
        'special': row.special,
        'display': row.display,
        'camera': row.camera,
        'form_factor': row.form_factor,
        'battery_power': row.battery_power,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'manufacture_address': row.manufacture_address,
        'generic_name': row.generic_name,
        'features': features
    }
    return render(request, 'Mobiles/iphone12mini.html', context=context)

def nokia34(request):
    row = Mobiles.objects.get(product_id='MOB4')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/mobiles/nokia3.4/' + str(row.image1),
        'image2': '../static/images/mobiles/nokia3.4/' + str(row.image2),
        'image3': '../static/images/mobiles/nokia3.4/' + str(row.image3),
        'image4': '../static/images/mobiles/nokia3.4/' + str(row.image4),
        'image5': '../static/images/mobiles/nokia3.4/' + str(row.image5),
        'os': row.os,
        'ram': row.ram,
        'product_dimensions': row.product_dimensions,
        'batteries': row.batteries,
        'item_model_number': row.item_model_number,
        'wireless': row.wireless,
        'special': row.special,
        'display': row.display,
        'camera': row.camera,
        'form_factor': row.form_factor,
        'battery_power': row.battery_power,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'manufacture_address': row.manufacture_address,
        'generic_name': row.generic_name,
        'features': features
    }
    return render(request, 'Mobiles/nokia3.4.html', context=context)

def vivoy20(request):
    row = Mobiles.objects.get(product_id='MOB5')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/mobiles/vivoy20/' + str(row.image1),
        'image2': '../static/images/mobiles/vivoy20/' + str(row.image2),
        'image3': '../static/images/mobiles/vivoy20/' + str(row.image3),
        'image4': '../static/images/mobiles/vivoy20/' + str(row.image4),
        'image5': '../static/images/mobiles/vivoy20/' + str(row.image5),
        'os': row.os,
        'ram': row.ram,
        'product_dimensions': row.product_dimensions,
        'batteries': row.batteries,
        'item_model_number': row.item_model_number,
        'wireless': row.wireless,
        'special': row.special,
        'display': row.display,
        'camera': row.camera,
        'form_factor': row.form_factor,
        'battery_power': row.battery_power,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'manufacture_address': row.manufacture_address,
        'generic_name': row.generic_name,
        'features': features
    }
    return render(request, 'Mobiles/vivoy20.html', context=context)