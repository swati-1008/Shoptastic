from django.shortcuts import render
from .models import *

# Create your views here.

def zeellehenga(request):
    row = Clothing.objects.get(product_id='CLO1')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': '../static/images/clothing/zeellehenga/' + str(row.image1),
        'image2': '../static/images/clothing/zeellehenga/' + str(row.image2),
        'image3': '../static/images/clothing/zeellehenga/' + str(row.image3),
        'image4': '../static/images/clothing/zeellehenga/' + str(row.image4),
        'image5': '../static/images/clothing/zeellehenga/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features
    }
    return render(request, 'Clothing/zeellehenga.html', context=context)

def babyjumpsuit(request):
    row = Clothing.objects.get(product_id='CLO6')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': '../static/images/clothing/taslarbabyjumpsuit/' + str(row.image1),
        'image2': '../static/images/clothing/taslarbabyjumpsuit/' + str(row.image2),
        'image3': '../static/images/clothing/taslarbabyjumpsuit/' + str(row.image3),
        'image4': '../static/images/clothing/taslarbabyjumpsuit/' + str(row.image4),
        'image5': '../static/images/clothing/taslarbabyjumpsuit/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features
    }
    return render(request, 'Clothing/babyjumpsuit.html', context=context)

def mensweatshirt(request):
    row = Clothing.objects.get(product_id='CLO3')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': '../static/images/clothing/mensweatshirt/' + str(row.image1),
        'image2': '../static/images/clothing/mensweatshirt/' + str(row.image2),
        'image3': '../static/images/clothing/mensweatshirt/' + str(row.image3),
        'image4': '../static/images/clothing/mensweatshirt/' + str(row.image4),
        'image5': '../static/images/clothing/mensweatshirt/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features
    }
    return render(request, 'Clothing/mensweatshirt.html', context=context)

def menshirt(request):
    row = Clothing.objects.get(product_id='CLO4')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': '../static/images/clothing/menshirt/' + str(row.image1),
        'image2': '../static/images/clothing/menshirt/' + str(row.image2),
        'image3': '../static/images/clothing/menshirt/' + str(row.image3),
        'image4': '../static/images/clothing/menshirt/' + str(row.image4),
        'image5': '../static/images/clothing/menshirt/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features
    }
    return render(request, 'Clothing/menshirt.html', context=context)

def babyromper(request):
    row = Clothing.objects.get(product_id='CLO5')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': '../static/images/clothing/babyromper/' + str(row.image1),
        'image2': '../static/images/clothing/babyromper/' + str(row.image2),
        'image3': '../static/images/clothing/babyromper/' + str(row.image3),
        'image4': '../static/images/clothing/babyromper/' + str(row.image4),
        'image5': '../static/images/clothing/babyromper/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features
    }
    return render(request, 'Clothing/babyromper.html', context=context)

def bandhejsaree(request):
    row = Clothing.objects.get(product_id='CLO2')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': '../static/images/clothing/bandhejsaree/' + str(row.image1),
        'image2': '../static/images/clothing/bandhejsaree/' + str(row.image2),
        'image3': '../static/images/clothing/bandhejsaree/' + str(row.image3),
        'image4': '../static/images/clothing/bandhejsaree/' + str(row.image4),
        'image5': '../static/images/clothing/bandhejsaree/' + str(row.image5),
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
        'features': features
    }
    return render(request, 'Clothing/bandhejsaree.html', context=context)