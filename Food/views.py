# DJANGO IMPORTS

# Import necessary functions for rendering, redirecting, and getting objects or 404 if not found
from django.shortcuts import render, redirect, get_object_or_404

# Default storage system for file handling
from django.core.files.storage import default_storage

# Import default User model for authentication
from django.contrib.auth.models import User

# Functions for user authentication
from django.contrib.auth import login, logout, authenticate

# Decorator for requiring login to access a view
from django.contrib.auth.decorators import login_required

# Messaging framework for storing simple messages
from django.contrib import messages

# Import the Recipe model from the current app
from .models import Recipe


# ---------------------
# Home Page
# ---------------------
def home(request):
    return render(request, 'home.html', context={'page_name': 'Food App'})


# ---------------------
# Add Recipe
# ---------------------
@login_required(login_url='/sign-in')
def add_recipe(request):
    add_recipe_name = None
    add_recipe_description = None
    add_recipe_image = None

    if request.method == 'POST':
        add_recipe_name = request.POST.get('add-form_recipe_name')
        add_recipe_description = request.POST.get('add-form_recipe_description')
        add_recipe_image = request.FILES.get('add-form_recipe_image')

        Recipe.objects.create(
            user = request.user,
            username = request.user.username,
            recipe_name=add_recipe_name,
            recipe_description=add_recipe_description,
            recipe_image=add_recipe_image
        )

        return redirect('/show-recipe')

    return render(request, 'add_recipe.html', context={'page_name': 'Add Recipes'})


# ---------------------
# Show Recipes
# ---------------------
@login_required(login_url='/sign-in')
def show_recipe(request):
    recipe_obj = Recipe.objects.all()

    # Filter recipes based on search query (HTTP GET request)
    if request.GET.get('search'):
        recipe_obj = recipe_obj.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': recipe_obj, 'page_name': 'Recipe List'}

    return render(request, 'show_recipe.html', context)


# ---------------------
# Update Recipe
# ---------------------
def update_recipe(request, url_slug):
    # Retrieve the recipe instance
    recipe_obj = Recipe.objects.get(slug=url_slug)

    if request.method == 'POST':
        update_recipe_name = request.POST.get('update-form_recipe_name')
        update_recipe_description = request.POST.get('update-form_recipe_description')
        update_recipe_image = request.FILES.get('update-form_recipe_image')

        # Update the recipe instance
        recipe_obj.recipe_name = update_recipe_name
        recipe_obj.recipe_description = update_recipe_description
        recipe_obj.recipe_image = update_recipe_image
        recipe_obj.save()

        return redirect('show_recipe_page')

    context = {'recipes': recipe_obj, 'page_name': 'Update Recipes'}
    return render(request, 'update_recipe.html', context)


# ---------------------
# Delete Recipe
# ---------------------
def delete_recipe(request,ID):
    # Retrieve the recipe instance
    recipe_obj = get_object_or_404(Recipe, id=ID)

    # Delete the recipe from the database
    recipe_obj.delete()

    # Get the path to the media file
    media_path = recipe_obj.recipe_image.path

    # Delete the associated media file
    if default_storage.exists(media_path):
        default_storage.delete(media_path)

    return redirect('show_recipe_page')


# ---------------------
# User Registration
# ---------------------
def register(request):
    if request.method == "POST":
        add_name = request.POST.get('register-form_name')
        add_username = request.POST.get('register-form_username')
        add_password = request.POST.get('register-form_password')

        if User.objects.filter(username=add_username).exists():
            messages.warning(request, "Username already exists.")
            return redirect('register_page')
        else:
            user_obj = User.objects.create(
                first_name=add_name,
                username=add_username
            )
            user_obj.set_password(add_password)
            user_obj.save()
            return redirect('sign_in_page')

    context = {'page_name': 'Registration'}
    return render(request, 'register.html', context)


# ---------------------
# User Sign-In
# ---------------------
def sign_in(request):
    if request.method == "POST":
        add_username = request.POST.get('sign-in-form_username')
        add_password = request.POST.get('sign-in-form_password')

        # Check Errors
        if not User.objects.filter(username=add_username).exists():
            messages.warning(request, "Invalid Username.")
            return redirect('sign_in_page')
        else:
            user = authenticate(username=add_username, password=add_password)

            if user:
                login(request, user)
            else:
                messages.warning(request, "Invalid Password.")
                return redirect('add_recipe_page')

    context = {'page_name': 'Sign In'}
    return render(request, 'sign_in.html', context)


# ---------------------
# User Sign-Out
# ---------------------
def sign_out(request):
    logout(request)
    return redirect('sign_in_page')