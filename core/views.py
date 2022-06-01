from django.shortcuts import render


def index(request):
    print('------------------------------------------------------------------------------------------------------')
    print(f'{dir(request)}')
    print(f'Method: {request.method}')
    #(f"headers: {request.headers}")
    print('------------------------------------------------------------------------------------------------------')
    print(f"Dir Requests: {dir(request.user)}")
    print(f"user tests: {request.user.user_permissions}")

    if str(request.user) == 'AnonymousUser':
        login = 'The user is anonymous'
    else:
        login = f'the user is: {request.user}'

    context = {
        'course': 'Dev with Django framework',
        'other': 'Django is Great !',
        'login': login
    }
    return render(request, 'index.html', context)


def concact(request):
    return render(request, 'contact.html')
