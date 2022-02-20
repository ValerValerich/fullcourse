from django.shortcuts import render
from .models import *
from .forms import *


def index(request):

    return render(request, 'myapp/index.html')

def about(request):
    maketform = MaketsForm()
    data = {
        'maketform': maketform
    }
    return render(request, 'myapp/about.html', data)

def prod(request):
    prodform = NomenlatsForm()
    data = {
        'prodform': prodform
    }
    # prods = Nomenklats.objects.all()
    return render(request, 'myapp/prod.html', data)

def comm(request):
    commform = CommForm()
    data = {
        'commform': commform
    }
    return render(request, 'myapp/comm.html', data)

