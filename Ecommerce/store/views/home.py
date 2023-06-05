from django.shortcuts import render , redirect , HttpResponseRedirect
from django.urls import reverse
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.db.models import Q
from django.core.paginator import PageNotAnInteger , Paginator, EmptyPage
from urllib.parse import urlencode


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        # get the current page number from the query string
        current_page = request.GET.get('page')

        # construct the redirect URL with the current page number
        if current_page:
            query_params = urlencode({'page': current_page})
            return redirect(f"{reverse('homepage')}?{query_params}")
        else:
            return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    query = request.GET.get('query')
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Paginator(Product.objects.filter(category=categoryID),2)

    elif query:
        products = Paginator(Product.objects.filter(name__icontains=query),2)

    else :
        products = Paginator(Product.objects.all(),2)
    page = request.GET.get('page')

    try:
        products = products.page(page)
    except PageNotAnInteger:
        products = products.page(1)
    except EmptyPage:
        products = products.page(products.num_pages)

    data = {}
    data['products'] = products
    data['categories'] = categories


    print('you are : ', request.session.get('email'))
    return render(request, 'store/index.html', data)
