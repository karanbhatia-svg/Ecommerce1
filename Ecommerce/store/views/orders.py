from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password

from django.views import View

from store.models.product import Product
from store.models.orders import Order
# from store.middlewares.auth import auth_middleware
from django.contrib.auth.models import User

class OrderView(View):


    def get(self , request ):
        User = request.session.get('User')
        orders = Order.get_orders_by_customer(User)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})