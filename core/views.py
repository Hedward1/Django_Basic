from django.shortcuts import render


def index(request):
    context = {
        'course': 'Dev with Django framework',
        'other': 'Django is Great !'
    }
    return render(request, 'index.html', context)


def concact(request):
    return render(request, 'contact.html')
