from django.contrib import admin
from django.urls import path

from .view1 import signup, order1
from .views.home import Index , store
from . import view1
# from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from . import view1


# from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),



    # path('login', Login.as_view(), name='login'),
    # path('logout', logout , name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    # path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
    path('signup', view1.signup, name='signup'),
    path('order1', view1.order1, name='order1'),
    path('dashboard', view1.dashboard, name='dashboard'),
    path('orderhistory', view1.orderhistory, name='orderhistory'),
    path('logout', view1.logout, name='logout'),
path('login', view1.login_request, name='login_request'),
path('edit_profile', view1.edit_profile, name='edit_profile'),
# path('check-out', view1.checkout, name='checkout')
]