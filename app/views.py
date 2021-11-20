from django.shortcuts import render
from .models import Spesial, Terbaru, Menu

# Create your views here.
# def index(request):
#     spesials = Spesial.objects.all()
#     terbarus = Terbaru.objects.all()
#     menus = Menu.objects.all()
#     return render(request, 'index.html', {'spesials': spesials})
#     return render(request, 'index.html', {'terbarus': terbarus})
#     return render(request, 'index.html', {'menus': menus})

def index(request):
    spesials = Spesial.objects.all()
    terbarus = Terbaru.objects.all()
    menus = Menu.objects.all()
    return render(request, 'index.html', {'spesials':spesials, 'terbarus':terbarus, 'menus':menus})


    # return render(request, 'index.html', {'terbarus':terbarus})

    # return render(request, 'index.html', {'menus':menus})