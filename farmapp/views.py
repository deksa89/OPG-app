from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

from .models import Product, Farm
from .forms import ProductForm, CustomUserCreationForm, EditUserProfileForm


@login_required
def list_products(request):
    products = Product.objects.all()
    user_profile = Farm.objects.get(user=request.user)
    return render(request, 'farmapp/product_list.html', {'products': products, 'user_profile': user_profile})

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
            product.farm = user_farm
            product.save()
            return redirect('list_products')
    else:
        form = ProductForm()

    return render(request, 'farmapp/add_product.html', {'form': form})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'farmapp/product_details.html', {'product': product})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.farm.user != request.user:
        return redirect('list_products')

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products') 
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


@login_required
def edit_profile(request):
    profile = get_object_or_404(Farm, user=request.user)

    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')  # Redirect to the profile view
    else:
        form = EditUserProfileForm(instance=profile)

    return render(request, 'farmapp/edit_profile.html', {'form': form})


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
