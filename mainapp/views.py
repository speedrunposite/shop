from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import DetailView

from .models import *

def index(request):
    # тут вернем шаблон
    tiles = LatestProducts.objects.get_products_for_main_page('tile')
    stairs =  LatestProducts.objects.get_products_for_main_page('stair')
    return render(request, 'main/index.html', {'tiles': tiles, 'stairs':stairs})

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