from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def index(request):

    """print('------------------------------------------------------------------------------------------------------')
    print(f'{dir(request)}')
    print(f'Method: {request.method}')
    #(f"headers: {request.headers}")
    print('------------------------------------------------------------------------------------------------------')
    print(f"Dir Requests: {dir(request.user)}")
    print(f"user tests: {request.user.user_permissions}")

    if str(request.user) == 'AnonymousUser':
        login = 'The user is anonymous'
    else:
        login = f'the user is: {request.user}'"""

    products = Product.objects.all()

    context = {
        'course': 'Dev with Django framework',
        'other': 'Django is Great !',
        'products': products
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    #prod = Product.objects.get(id=pk)
    prod = get_object_or_404(Product, id=pk)

    context = {
        'product': prod
    }
    return render(request, 'product.html', context)


def error404(request, excption):
    return render(request, '404.html')


