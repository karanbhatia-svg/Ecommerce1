from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from store.forms import CustomerForm

class Signup(View):
    def signup(request):
        page = 'register'
        form = CustomerForm()
        if request.method == 'POST':
            form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('gallery')
                context = {'form': form, 'page': page}
                return render(request, 'signup/signup.html', context)
