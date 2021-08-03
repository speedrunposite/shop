from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
<<<<<<< HEAD
from django.views.generic.detail import DetailView
=======
from django.views.generic import DetailView
>>>>>>> 772022faf32c447908057b0b14ae8a029dfc4e12

from .models import *

def index(request):
    # тут вернем шаблон
    products = LatestProducts.objects.get_products_for_main_page('tile', 'stair')
    return render(request, 'main/index.html', {'products': products})


def about(request):
    return render(request, 'main/about.html')


class TileListView(generic.ListView):

    model = Tile

    def get_queryset(self):
        return Tile.objects.order_by('title')


class StairListView(generic.ListView):

    model = Stair

    def get_queryset(self):
        return Stair.objects.order_by('title')
