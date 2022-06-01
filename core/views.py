from django.shortcuts import render


def index(request):
    print(dir(request))
    print(f'method: {request.method}')
    print(f'method: {request.headers}')

    context = {
        'course': 'Dev with Django framework',
        'other': 'Django is Great !'
    }
    return render(request, 'index.html', context)


def concact(request):
    return render(request, 'contact.html')
