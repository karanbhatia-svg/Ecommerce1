from django import forms

# Reordering Form and View


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models.orders import Order

class OrderForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super(CustomerForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': 'Enter username...'})
    #     self.fields['password1'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': 'Enter password...'})
    #     self.fields['password2'].widget.attrs.update(
    #         {'class': 'form-control', 'placeholder': 'Confirm password...'})







