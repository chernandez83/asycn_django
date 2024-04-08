from django.shortcuts import render

from async_api.api import api_slow


def index(request):
    return render(request, 'index.html')


def results(request):
    api_slow()
    context = {
        'res': 20,
    }
    return render(request, 'res.html', context)