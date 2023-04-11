from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm, OrderForm
from .models.product import Product
from .models.orders import Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CustomerForm()
	return render (request, "store/signup.html", context={"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="store/login.html", context={"form":form})
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("login_request")

def order1(request):
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = OrderForm()
	return render (request, "store/signup.html", context={"form":form})

def edit_profile(request):
	msg=None
	if request.method=='POST':
		form= CustomerForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			msg='Data has been saved'
	form= CustomerForm(instance=request.user)
	return render(request, 'store/edit-profile.html',{'form':form,'msg':msg})

def dashboard(request):
	return render(request, 'store/dashboard.html')

def orderhistory(request):
	return render(request, 'store/orderhistory.html')
def edit_profile(request):

	form = CustomerForm(instance=request.user)
	# profile_form = UpdateProfileForm(instance=request.user.profile)
	return render(request, 'store/edit-profile.html',{'form':form})


# def checkout(request):
# 	cart = request.session.get('cart')
# 	product = Product.get_products_by_id(list(cart.keys()))
#
# 	# Functions for finding total ammount
# 	def cart_quantity(product, cart):
# 		keys = cart.keys()
# 		for id in keys:
# 			if int(id) == product.id
# 				return cart.get(id)
# 		return 0;
#
# 	def price_total(product, cart):
# 		return product.price * cart_quantity(product, cart)
#
# 	def total_cart_price(products, cart):
# 		sum = 0;
# 		for p in products:
# 			sum += price_total(p, cart)
#
# 		return sum
#
# 	quantity1 = cart.get(str(Product.id))
# 	prof = Order(User=request.user, address=request.POST.get('address'), phone=request.POST.get('phone'),)
# 	prof.save()
# 	for product in product:
# 		print(cart.get(str(product.id)))
# 		prof1 = OrderItem(order=Order(id=Order),product=Product,quantity=cart.get(str(product.id)),)
# 		prof1.save()
# 		request.session['cart'] = {}
# 		return redirect('store/cart')


# cart = request.session.get('cart')
# product = Product.get_products_by_id(list(cart.keys()))

	# Functions for finding total ammount
# def cart_quantity(product, cart):
# 		keys = cart.keys()
# 		for id in keys:
# 			if int(id) == product.id
# 				return cart.get(id)
# 		return 0;
#
# 	def price_total(product, cart):
# 		return product.price * cart_quantity(product, cart)
#
# 	def total_cart_price(products, cart):
# 		sum = 0;
# 		for p in products:
# 			sum += price_total(p, cart)
#
# 		return sum
