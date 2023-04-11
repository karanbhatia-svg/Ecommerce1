from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password

from django.views import View
from django.contrib.auth.decorators import login_required
from store.models.product import Product
from store.models.orders import Order
from django.contrib.auth.decorators import login_required
from store.models.orders import Order
from django.contrib.auth.models import User



class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = request.user
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, user, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=User(id=user),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')