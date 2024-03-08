from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

from .models import Product, Farm
from .forms import ProductForm, CustomUserCreationForm


# Create your views here.
@login_required
def list_products(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'farmapp/product_list.html', {'products': products})

@login_required
def add_product(request):
    try:
        user_farm = Farm.objects.get(user=request.user)
        print("farma: ", user_farm)
    except Farm.DoesNotExist:
        print("farm doesnt exist")
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.farm = user_farm  # Set the product's farm to the user's farm
            product.save()
            # Redirect to a new URL:
            return redirect('list_products')  # Assuming 'product_list' is the URL name for listing products
    else:
        form = ProductForm()

    return render(request, 'farmapp/add_product.html', {'form': form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.farm.user != request.user:
        # If the product does not belong to the logged-in user, redirect or show an error
        return redirect('list_products')  # Replace with your appropriate URL

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')  # Replace with your appropriate URL
    else:
        form = ProductForm(instance=product)

    return render(request, 'farmapp/add_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('list_products')

@login_required
def view_profile(request):
    try:
        user_profile = Farm.objects.get(user=request.user)
        print("user_profile: ", user_profile)
    except Farm.DoesNotExist:
        user_profile = None
    return render(request, 'farmapp/profile.html', {'user_profile': user_profile})


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserProfileEditForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('view_profile')  # Redirect to the profile view
#     else:
#         form = UserProfileEditForm(instance=request.user)
#     return render(request, 'farmapp/edit_profile.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user: ", user)
            user.save()
            login(request, user)
            return redirect('list_products')
    else:
        form = CustomUserCreationForm()
    return render(request, 'farmapp/register.html', {'form': form})
