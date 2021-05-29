from django.shortcuts import render
from  .models import *

# Create your views here.

def mdfwalldecor(request):
    row = Furniture.objects.get(product_id='FUR1')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/furniture/mdfwalldecor/' + str(row.image1),
        'image2': '../static/images/furniture/mdfwalldecor/' + str(row.image2),
        'image3': '../static/images/furniture/mdfwalldecor/' + str(row.image3),
        'image4': '../static/images/furniture/mdfwalldecor/' + str(row.image4),
        'image5': '../static/images/furniture/mdfwalldecor/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'assembly_required': row.assembly_required,
        'primary_material': row.primary_material,
        'finish_type': row.finish_type,
        'item_shape': row.item_shape,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features[0]
    }
    return render(request, 'Furniture/mdfwalldecor.html', context=context)

def furniturecafestool(request):
    row = Furniture.objects.get(product_id='FUR2')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/furniture/furniturecafestool/' + str(row.image1),
        'image2': '../static/images/furniture/furniturecafestool/' + str(row.image2),
        'image3': '../static/images/furniture/furniturecafestool/' + str(row.image3),
        'image4': '../static/images/furniture/furniturecafestool/' + str(row.image4),
        'image5': '../static/images/furniture/furniturecafestool/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'assembly_required': row.assembly_required,
        'primary_material': row.primary_material,
        'finish_type': row.finish_type,
        'item_shape': row.item_shape,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features[0]
    }
    return render(request, 'Furniture/furniturecafestool.html', context=context)

def woodkeyholder(request):
    row = Furniture.objects.get(product_id='FUR3')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/furniture/woodkeyholder/' + str(row.image1),
        'image2': '../static/images/furniture/woodkeyholder/' + str(row.image2),
        'image3': '../static/images/furniture/woodkeyholder/' + str(row.image3),
        'image4': '../static/images/furniture/woodkeyholder/' + str(row.image4),
        'image5': '../static/images/furniture/woodkeyholder/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'assembly_required': row.assembly_required,
        'primary_material': row.primary_material,
        'finish_type': row.finish_type,
        'item_shape': row.item_shape,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features[0]
    }
    return render(request, 'Furniture/a10keyholder.html', context=context)

def storagecase(request):
    row = Furniture.objects.get(product_id='FUR4')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/furniture/storagecase/' + str(row.image1),
        'image2': '../static/images/furniture/storagecase/' + str(row.image2),
        'image3': '../static/images/furniture/storagecase/' + str(row.image3),
        'image4': '../static/images/furniture/storagecase/' + str(row.image4),
        'image5': '../static/images/furniture/storagecase/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'assembly_required': row.assembly_required,
        'primary_material': row.primary_material,
        'finish_type': row.finish_type,
        'item_shape': row.item_shape,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features[0]
    }
    return render(request, 'Furniture/storagecase.html', context=context)

def wallmirror(request):
    row = Furniture.objects.get(product_id='FUR5')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/furniture/wallmirror/' + str(row.image1),
        'image2': '../static/images/furniture/wallmirror/' + str(row.image2),
        'image3': '../static/images/furniture/wallmirror/' + str(row.image3),
        'image4': '../static/images/furniture/wallmirror/' + str(row.image4),
        'image5': '../static/images/furniture/wallmirror/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'assembly_required': row.assembly_required,
        'primary_material': row.primary_material,
        'finish_type': row.finish_type,
        'item_shape': row.item_shape,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features[0]
    }
    return render(request, 'Furniture/wallmirror.html', context=context)

def entunit(request):
    row = Furniture.objects.get(product_id='FUR6')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'color': row.colour,
        'image1': '../static/images/furniture/tventunit/' + str(row.image1),
        'image2': '../static/images/furniture/tventunit/' + str(row.image2),
        'image3': '../static/images/furniture/tventunit/' + str(row.image3),
        'image4': '../static/images/furniture/tventunit/' + str(row.image4),
        'image5': '../static/images/furniture/tventunit/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'assembly_required': row.assembly_required,
        'primary_material': row.primary_material,
        'finish_type': row.finish_type,
        'item_shape': row.item_shape,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features[0]
    }
    return render(request, 'Furniture/tventunit.html', context=context)