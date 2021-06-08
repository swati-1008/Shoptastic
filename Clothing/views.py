from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from datetime import date
import tensorflow as tf
import numpy as np
from django.db.models import Count

# Create your views here.

new_model = tf.keras.models.load_model('Machine learning models/stack.tf')

def zeellehenga(request):
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
            comment = Comments(pid = 'CLO1', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'CLO1', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'CLO1').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
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
    word_comments = Comments.objects.filter(pid = 'CLO1').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Clothing.objects.get(product_id='CLO1').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Clothing.objects.update_or_create(product_id='CLO1', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='CLO1')
    row = Clothing.objects.get(product_id='CLO1')
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
    return render(request, 'Clothing/zeellehenga.html', context=context)

def babyjumpsuit(request):
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
            comment = Comments(pid = 'CLO6', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'CLO6', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'CLO6').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
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
    word_comments = Comments.objects.filter(pid = 'CLO6').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Clothing.objects.get(product_id='CLO6').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Clothing.objects.update_or_create(product_id='CLO6', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='CLO6')
    row = Clothing.objects.get(product_id='CLO6')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': row.image1,
        'image2': row.image2,
        'image3': row.image3,
        'image4': row.image4,
        'image5': row.image5,
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
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
    return render(request, 'Clothing/babyjumpsuit.html', context=context)

def mensweatshirt(request):
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
            comment = Comments(pid = 'CLO3', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'CLO3', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'CLO3').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
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
    word_comments = Comments.objects.filter(pid = 'CLO3').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Clothing.objects.get(product_id='CLO3').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Clothing.objects.update_or_create(product_id='CLO3', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='CLO3')
    row = Clothing.objects.get(product_id='CLO3')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': row.image1,
        'image2': row.image2,
        'image3': row.image3,
        'image4': row.image4,
        'image5': row.image5,
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
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
    return render(request, 'Clothing/mensweatshirt.html', context=context)

def menshirt(request):
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
            comment = Comments(pid = 'CLO4', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'CLO4', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'CLO4').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
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
    word_comments = Comments.objects.filter(pid = 'CLO4').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Clothing.objects.get(product_id='CLO4').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Clothing.objects.update_or_create(product_id='CLO4', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='CLO4')
    row = Clothing.objects.get(product_id='CLO4')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': row.image1,
        'image2': row.image2,
        'image3': row.image3,
        'image4': row.image4,
        'image5': row.image5,
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
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
    return render(request, 'Clothing/menshirt.html', context=context)

def babyromper(request):
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
            comment = Comments(pid = 'CLO5', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'CLO5', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'CLO5').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
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
    word_comments = Comments.objects.filter(pid = 'CLO5').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Clothing.objects.get(product_id='CLO5').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Clothing.objects.update_or_create(product_id='CLO5', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='CLO5')
    row = Clothing.objects.get(product_id='CLO5')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': row.image1,
        'image2': row.image2,
        'image3': row.image3,
        'image4': row.image4,
        'image5': row.image5,
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
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
    return render(request, 'Clothing/babyromper.html', context=context)

def bandhejsaree(request):
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
            comment = Comments(pid = 'CLO2', uid = request.user, comment = cmt, rating = data, date = date.today())
            comment.save()
        elif cmt:
            required = '<i class="fas fa-exclamation-triangle" style="color: orange;"></i>   Please provide a rating first to submit your review!'
        elif data:
            comment = Comments(pid = 'CLO2', uid = request.user, rating = data, date = date.today())
            comment.save()
    fieldname = 'rating'
    rating_count = Comments.objects.filter(pid = 'CLO2').values(fieldname).order_by(fieldname).annotate(the_count = Count(fieldname))
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
    word_comments = Comments.objects.filter(pid = 'CLO2').exclude(comment = 'NULL')
    total_comments = len(word_comments)
    # for i in word_comments:
    #     print(i.comment)
    final_rating = round((rating_sum / total_ratings), 2)
    prev_model_rating = Clothing.objects.get(product_id='CLO2').model_rating
    if rating != 0:
        model_rating = round(((prev_model_rating * total_comments) + rating) / (total_comments + 1), 2)
    else:
        model_rating = prev_model_rating
    obj, created = Clothing.objects.update_or_create(product_id='CLO2', defaults={'average_customer_rating':final_rating, 'model_rating': model_rating})
    obj.save()
    rating1 = (rate1 / (total_ratings)) * 100
    rating2 = (rate2 / (total_ratings)) * 100
    rating3 = (rate3 / (total_ratings)) * 100
    rating4 = (rate4 / (total_ratings)) * 100
    rating5 = (rate5 / (total_ratings)) * 100
    final_star = final_rating * 20                          # () * 100 / 5 = () * 20
    model_star = model_rating * 20
    comments = Comments.objects.filter(pid='CLO2')
    row = Clothing.objects.get(product_id='CLO2')
    features = list(Features.objects.filter(pid=row))
    context = {
        'product_name': row.product_name,
        'product_specs': row.product_desc,
        'price': row.price,
        'image1': row.image1,
        'image2': row.image2,
        'image3': row.image3,
        'image4': row.image4,
        'image5': row.image5,
        'product_dimensions': row.product_dimensions,
        'manufacturer': row.manufacturer,
        'origin': row.origin,
        'asin': row.asin,
        'average_customer_rating': row.average_customer_rating,
        'best_sellers': row.best_sellers,
        'launch_date': row.launch_date,
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
    return render(request, 'Clothing/bandhejsaree.html', context=context)