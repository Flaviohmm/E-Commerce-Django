# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

from .forms import ConatctForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ConatctForm(request.POST)
    else:
        form = ConatctForm()

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
