from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def concact(request):
    return render(request, 'contact.html')
