from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm, PostForm, RecipeForm, SubscribeForm

# Pagination
from django.core.paginator import Paginator

# API
import requests
import json

# Models
from .models import *

# Windows Email
import webbrowser

# SAMPLE API TESTER HERE - FOR DEVELOPMENT ONLY
# from .sampleapi import *

# API Information here
baseurl = 'https://api.spoonacular.com/recipes/'
apiKey = '4720b9d539c341cf8963a42738560595'

# ---------------------------------------------------------------
# Create your views here.

# Home page
@login_required(login_url="/login/")
def index(request):

    simpleform = RecipeForm()
    
    # Display some random recipes
    params = {
        'apiKey': apiKey,
        'number': '6'
    }
    display = requests.get(baseurl + "/random", params=params).json()["recipes"]
   
    try:
        subscribed = Subscribe.objects.get(person=request.user).subscribed
    except:
        subscribed = None

    sub_form = SubscribeForm()

    return render(request, "home/index.html", {
        'sub_form': sub_form,
        "subscribed": subscribed,
        'simpleform': simpleform,
        'display': display
    })


# About page
@login_required(login_url="/login/")
def about(request):

    contact_form = ContactForm()
    simpleform = RecipeForm()

    # Submit via contactform to email
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = "%0D%0A".join(form.cleaned_data.get("message").splitlines())
            recipient = "mpark1994@outlook.com"

            webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + message, new=1)

    return render(request, "home/about.html", {
        'contact_form': contact_form,
        'simpleform': simpleform
    })


# Contact page
@login_required(login_url="/login/")
def contact(request):

    sub_form = SubscribeForm()
    contact_form = ContactForm()
    simpleform = RecipeForm()

    try:
        subscribed = Subscribe.objects.get(person=request.user).subscribed
    except:
        subscribed = None

    # Submit via contactform to email
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            message = "%0D%0A".join(form.cleaned_data.get("message").splitlines())
            recipient = "mpark1994@outlook.com"

            webbrowser.open('mailto:?to=' + recipient + '&subject=' + subject + '&body=' + message, new=1)

    return render(request, "home/contact.html", {
        'sub_form': sub_form,
        'contact_form': contact_form,
        'subscribed': subscribed,
        'simpleform': simpleform
    })


# Recipe page
@login_required(login_url="/login/")
def recipe_post(request, id):

    recipeform = RecipeForm()
    simpleform = RecipeForm()

    params = {
        'apiKey': apiKey,
        'includeNutrition': "false"
    }
    recipe_info = requests.get(baseurl + str(id) + "/information", params=params).json()

    # To get iteration for star rating
    range_num = range(recipe_info["healthScore"] // 20)

    # For comment form
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get("message")
            subject = form.cleaned_data.get("subject")
            new_comment = Comment(recipe_id=id, person=request.user, subject=subject, comment=comment,)
            new_comment.save()

            form = PostForm()

            return redirect(recipe_post, id)
    else:
        form = PostForm()

    # Try to get comments, if none, return ""
    try:
        comments = [comment.serialize() for comment in Comment.objects.filter(recipe_id=id)]

        # Paginate the comments
        p = Paginator(comments, 10)
        page = request.GET.get('page')
        comments = p.get_page(page)
    except:
        comments = None

    # Try to get favorites, if none, return ""
    try:
        favorited = Favorite.objects.get(recipe_id=id, person=request.user).favorited
    except:
        favorited = None

    return render(request, "home/recipe-post.html", {
        "form": form,
        "recipes": recipe_info,
        "comments": comments,
        "range": range_num,
        "favorited": favorited,
        "recipeform": recipeform,
        'simpleform': simpleform
    })


# Recipe comment
@login_required(login_url="/login/")
def recipe_comment(request, post_id):

    # Query for requested post
    try:
        comment = Comment.objects.get(id=post_id)
    except Comment.DoesNotExist:
        comment = None

    if comment:
        comment.delete()
    return

# Recipe comment
@login_required(login_url="/login/")
def subscribe(request):

    if request.method == "POST":
        form = SubscribeForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")

            # Check if already subbed
            try:
                subscribed = Subscribe.objects.get(email=email, person=request.user)
                subscribed.subscribed = not subscribed.subscribed
                subscribed.save()
            # If new subscriber
            except:
                new_subscriber = Subscribe(email=email, person=request.user, subscribed=True)
                new_subscriber.save()

    return redirect(index)

@login_required(login_url="/login/")
def recipe_favorite(request, post_id):

    # Check if already favorited
    try:
        favorited = Favorite.objects.get(recipe_id=post_id, person=request.user)
        favorited.favorited = not favorited.favorited
        favorited.save()
    # If new subscriber
    except:
        new_favorited = Favorite(recipe_id=post_id, person=request.user, favorited=True)
        new_favorited.save()

    return redirect(recipe_post, id=post_id)


# Recipe finder
@login_required(login_url="/login/")
def recipe_finder(request, diet):

    simpleform = RecipeForm()
    form = RecipeForm()
    recipe_list = None
    query = None

    if request.method == "GET":
        if diet == "standard":
            params = {
                'apiKey': apiKey,
                'number': '20'
            }
            recipe_list = requests.get(baseurl + "/random", params=params).json()['recipes']

        else:
            params = {
                'apiKey': apiKey,
                'tag': diet,
                'number': '20'
            }
            recipe_list = requests.get(baseurl + "/random", params=params).json()['recipes']

    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get("query")
            ingredients = ",".join(form.cleaned_data.get("ingredients").replace('!@#$%^&*()[]{};:,./<>?\|`~-=_+', ' ').split())
            diet = form.cleaned_data.get("diet")

            if diet == "standard":
                params = {
                    'apiKey': apiKey,
                    'query': query,
                    'includeIngredients': ingredients
                }
            else:
                params = {
                    'apiKey': apiKey,
                    'query': query,
                    'diet': diet,
                    'includeIngredients': ingredients
                }
            recipe_list = requests.get(baseurl + "/complexSearch", params=params).json()["results"]
            

    # Paginate the recipes
    p = Paginator(recipe_list, 10)
    page = request.GET.get('page')
    recipe_list = p.get_page(page)
    
    return render(request, "home/recipe-finder.html", {
        'recipes': recipe_list,
        'query': query,
        'form': form,
        'simpleform': simpleform
    })

# User Profile
@login_required(login_url="/login/")
def profile(request, user):

    simpleform = RecipeForm()

    # Check to see if user exists
    try:
        current_user = User.objects.get(username=user)
    except:
        return redirect(index)

    # Query user favorite recipes
    try: 
        favorites = ",".join([str(favorite.serialize()['recipe']) for favorite in Favorite.objects.filter(person=current_user, favorited=True)])

        params = {
            'apiKey': apiKey,
            'ids': favorites
        }
        favorites = requests.get(baseurl + "/informationBulk", params=params).json()

        p = Paginator(favorites, 9)
        page = request.GET.get('page')
        favorites = p.get_page(page)
        
    except:
        favorites = None

    return render(request, "home/profile.html", {
        'simpleform': simpleform,
        'user': current_user,
        'favorites': favorites
    })