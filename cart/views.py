# cart/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Categories
from collections import Counter

def add_to_cart(request, item_id):
    # Get the current cart from cookies
    cart = request.COOKIES.get('cart', '')
    cart_items = cart.split(',')[1:]

    if str(item_id) in cart_items:
        # If item is already in the cart, increment its quantity
        cart_items.append(str(item_id))
    else:
        # If item is not in the cart, add it with quantity 1
        cart_items.append(str(item_id))

    updated_cart = f',{",".join(cart_items)}'
    response = redirect('cart:cart_detail')
    response.set_cookie('cart', updated_cart)

    return response

def remove_from_cart(request, item_id):
    # Get the current cart from cookies
    cart = request.COOKIES.get('cart', '')
    cart_items = cart.split(',')[1:]

    if str(item_id) in cart_items:
        # If item is in the cart, decrement its quantity
        cart_items.remove(str(item_id))

    updated_cart = f',{",".join(cart_items)}'
    response = redirect('cart:cart_detail')
    response.set_cookie('cart', updated_cart)

    return response

def remove_item(request, item_id):
    # Get the current cart from cookies
    cart = request.COOKIES.get('cart', '')
    cart_items = cart.split(',')[1:]

    if str(item_id) in cart_items:
        # If item is in the cart, remove it completely
        cart_items = [item for item in cart_items if item != str(item_id)]

    updated_cart = f',{",".join(cart_items)}'
    response = redirect('cart:cart_detail')
    response.set_cookie('cart', updated_cart)

    return response

def cart_detail(request):
    cart = request.COOKIES.get('cart', '')
    cart_items = cart.split(',')[1:]

    cart_item_counter = Counter(cart_items)

    # Initialize an empty dictionary
    cart_item_quantities = {}

    # Loop through the cart_item_counter to build the dictionary, but check if the item_id is numeric
    for item_id, count in cart_item_counter.items():
        if item_id.isdigit():  # Check if the item_id is numeric
            cart_item_quantities[int(item_id)] = count

    cart_items = Item.objects.filter(pk__in=cart_item_quantities.keys())
    available_items = Item.objects.exclude(pk__in=cart_item_quantities.keys())

    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'available_items': available_items, 'cart_item_quantities': cart_item_quantities})


def dropdown(request):
    categories = Categories.objects.all()

    return render(request, 'cart/dropdown.html', {'categories':categories})