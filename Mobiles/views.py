from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from datetime import date
# import tensorflow as tf
# import numpy as np
from django.db.models import Count

# Create your views here.

# new_model = tf.keras.models.load_model('Machine learning models/stack.tf')

def oneplus(request):
    rating = 0
    required = ''
    if request.method == "POST":
        # product_id can also be received with this code (with correct code - not implemented yet)
        # Check request.POST -> product_id is also returned
        data = request.POST.get('rate_value')
        cmt = request.POST.get('comment')
        if data and cmt:
            if cmt:
                # predictions = new_model.predict([cmt])
                # rating = np.argmax(predictions[0])
                pass
            comment = Comments(pid = 'MOB1', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'MOB1', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
    rate1 = 0
    rate2 = 0
    rate3 = 0
    rate4 = 0
    rate5 = 0
    for i in rating_count:
        if i.get("rating") == 1.0:
            rate1 = i.get("the_count")
        elif i.get("rating") == 2.0:
            rate2 = i.get("the_count")
        elif i.get("rating") == 3.0:
            rate3 = i.get("the_count")
        elif i.get("rating") == 4.0:
            rate4 = i.get("the_count")
        elif i.get("rating") == 5.0:
            rate5 = i.get("the_count")
    rating_sum = rate1 * 1 + rate2 * 2 + rate3 * 3 + rate4 * 4 + rate5 * 5
    total_ratings = rate1 + rate2 + rate3 + rate4 + rate5
    word_comments = Comments.objects.exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    final_rating = rating_sum / total_ratings
    prev_model_rating = Mobiles.objects.get(product_id='MOB1').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Mobiles.objects.update_or_create(product_id='MOB1', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='MOB1')
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
        'wireless': row.wireless_features,
        'special': row.special_features,
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
        'features': features,
        'comments': comments,
        'final_rating': row.average_customer_rating,
        'total_ratings': total_ratings,
        'rating1': rating5,
        'rating2': rating4,
        'rating3': rating3,
        'rating4': rating2,
        'rating5': rating1,
        'final_star': final_star,
        'model_rating': row.model_rating,
        'model_star': model_star,
        'comments': word_comments,
        'required': required,
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