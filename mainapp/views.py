from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from django.views.generic import DetailView

from .models import *

def index(request):
    # тут вернем шаблон
    tiles = LatestProducts.objects.get_products_for_main_page('tile')
    stairs =  LatestProducts.objects.get_products_for_main_page('stair')
    return render(request, 'main/index.html', {'tiles': tiles, 'stairs':stairs})
>>>>>>> b08b45918ea7fce339bd8858c76e1ff09a7a0514
=======
from django.views import generic
from django.views.generic.detail import DetailView
from .models import *

def index(request):
    return render(request, 'main/index.html')
>>>>>>> ee537a309fb7aa10c57ba6c58d0c8e658749658a

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