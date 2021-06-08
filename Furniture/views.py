from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from datetime import date
import tensorflow as tf
import numpy as np
from django.db.models import Count

# Create your views here.

new_model = tf.keras.models.load_model('Machine learning models/stack.tf')

def mdfwalldecor(request):
    rating = 0
    required = ''
    if request.method == "POST":
        # product_id can also be received with this code (with correct code - not implemented yet)
        # Check request.POST -> product_id is also returned
        data = request.POST.get('rate_value')
        cmt = request.POST.get('comment')
        if data and cmt:
            predictions = new_model.predict([cmt])
            rating = np.argmax(predictions[0])
            print(f'COMMENT = {cmt}, MODEL PREDICTED RATING = {rating}')
            comment = Comments(pid = 'FUR1', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'FUR1', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'FUR1').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
    # print(rating_count)
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
    word_comments = Comments.objects.filter(pid = 'FUR1').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    print(f'rate1 = {rate1}, rate2 = {rate2}, rate3 = {rate3}, rate4 = {rate4}, rate5 = {rate5}')
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Furniture.objects.get(product_id='FUR1').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Furniture.objects.update_or_create(product_id='FUR1', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='FUR1')
    row = Furniture.objects.get(product_id='FUR1')
    features = Features.objects.filter(pid=row)
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
        'features': features[0],
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
    return render(request, 'Furniture/mdfwalldecor.html', context=context)

def furniturecafestool(request):
    rating = 0
    required = ''
    if request.method == "POST":
        # product_id can also be received with this code (with correct code - not implemented yet)
        # Check request.POST -> product_id is also returned
        data = request.POST.get('rate_value')
        cmt = request.POST.get('comment')
        if data and cmt:
            predictions = new_model.predict([cmt])
            rating = np.argmax(predictions[0])
            print(f'COMMENT = {cmt}, MODEL PREDICTED RATING = {rating}')
            comment = Comments(pid = 'FUR2', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'FUR2', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'FUR2').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
    # print(rating_count)
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
    word_comments = Comments.objects.filter(pid = 'FUR2').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    print(f'rate1 = {rate1}, rate2 = {rate2}, rate3 = {rate3}, rate4 = {rate4}, rate5 = {rate5}')
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Furniture.objects.get(product_id='FUR2').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Furniture.objects.update_or_create(product_id='FUR2', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='FUR2')
    row = Furniture.objects.get(product_id='FUR2')
    features = Features.objects.filter(pid=row)
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
        'features': features[0],
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
    return render(request, 'Furniture/furniturecafestool.html', context=context)

def woodkeyholder(request):
    rating = 0
    required = ''
    if request.method == "POST":
        # product_id can also be received with this code (with correct code - not implemented yet)
        # Check request.POST -> product_id is also returned
        data = request.POST.get('rate_value')
        cmt = request.POST.get('comment')
        if data and cmt:
            predictions = new_model.predict([cmt])
            rating = np.argmax(predictions[0])
            print(f'COMMENT = {cmt}, MODEL PREDICTED RATING = {rating}')
            comment = Comments(pid = 'FUR3', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'FUR3', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'FUR3').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
    # print(rating_count)
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
    word_comments = Comments.objects.filter(pid = 'FUR3').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    print(f'rate1 = {rate1}, rate2 = {rate2}, rate3 = {rate3}, rate4 = {rate4}, rate5 = {rate5}')
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Furniture.objects.get(product_id='FUR3').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Furniture.objects.update_or_create(product_id='FUR3', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='FUR3')
    row = Furniture.objects.get(product_id='FUR3')
    features = Features.objects.filter(pid=row)
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
        'features': features[0],
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
    return render(request, 'Furniture/a10keyholder.html', context=context)

def storagecase(request):
    rating = 0
    required = ''
    if request.method == "POST":
        # product_id can also be received with this code (with correct code - not implemented yet)
        # Check request.POST -> product_id is also returned
        data = request.POST.get('rate_value')
        cmt = request.POST.get('comment')
        if data and cmt:
            predictions = new_model.predict([cmt])
            rating = np.argmax(predictions[0])
            print(f'COMMENT = {cmt}, MODEL PREDICTED RATING = {rating}')
            comment = Comments(pid = 'FUR4', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'FUR4', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'FUR4').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
    # print(rating_count)
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
    word_comments = Comments.objects.filter(pid = 'FUR4').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    print(f'rate1 = {rate1}, rate2 = {rate2}, rate3 = {rate3}, rate4 = {rate4}, rate5 = {rate5}')
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Furniture.objects.get(product_id='FUR4').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Furniture.objects.update_or_create(product_id='FUR4', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='FUR4')
    row = Furniture.objects.get(product_id='FUR4')
    features = Features.objects.filter(pid=row)
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
        'features': features[0],
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
    return render(request, 'Furniture/storagecase.html', context=context)

def wallmirror(request):
    rating = 0
    required = ''
    if request.method == "POST":
        # product_id can also be received with this code (with correct code - not implemented yet)
        # Check request.POST -> product_id is also returned
        data = request.POST.get('rate_value')
        cmt = request.POST.get('comment')
        if data and cmt:
            predictions = new_model.predict([cmt])
            rating = np.argmax(predictions[0])
            print(f'COMMENT = {cmt}, MODEL PREDICTED RATING = {rating}')
            comment = Comments(pid = 'FUR5', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'FUR5', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'FUR5').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
    # print(rating_count)
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
    word_comments = Comments.objects.filter(pid = 'FUR5').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    print(f'rate1 = {rate1}, rate2 = {rate2}, rate3 = {rate3}, rate4 = {rate4}, rate5 = {rate5}')
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Furniture.objects.get(product_id='FUR5').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Furniture.objects.update_or_create(product_id='FUR5', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='FUR5')
    row = Furniture.objects.get(product_id='FUR5')
    features = Features.objects.filter(pid=row)
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
        'features': features[0],
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
    return render(request, 'Furniture/wallmirror.html', context=context)

def entunit(request):
    rating = 0
    required = ''
    if request.method == "POST":
        # product_id can also be received with this code (with correct code - not implemented yet)
        # Check request.POST -> product_id is also returned
        data = request.POST.get('rate_value')
        cmt = request.POST.get('comment')
        if data and cmt:
            predictions = new_model.predict([cmt])
            rating = np.argmax(predictions[0])
            print(f'COMMENT = {cmt}, MODEL PREDICTED RATING = {rating}')
            comment = Comments(pid = 'FUR6', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'FUR6', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'FUR6').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
    # print(rating_count)
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
    word_comments = Comments.objects.filter(pid = 'FUR6').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    print(f'rate1 = {rate1}, rate2 = {rate2}, rate3 = {rate3}, rate4 = {rate4}, rate5 = {rate5}')
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Furniture.objects.get(product_id='FUR6').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Furniture.objects.update_or_create(product_id='FUR6', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='FUR6')
    row = Furniture.objects.get(product_id='FUR6')
    features = Features.objects.filter(pid=row)
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
        'features': features[0],
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
    return render(request, 'Furniture/tventunit.html', context=context)