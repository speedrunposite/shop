from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import DetailView

from .models import *

def index(request):
    # тут вернем шаблон
    products = LatestProducts.objects.get_products_for_main_page('tile', 'stair')
    tiles = LatestProducts.objects.get_products_for_main_page('tile')
    stairs = LatestProducts.objects.get_products_for_main_page('stair')
    paving_slabs = LatestProducts.objects.get_products_for_main_page('pavingslab')
    contacts = LatestProducts.objects.get_products_for_main_page('contact')
    return render(request, 'main/index.html',
     {'tiles': tiles, 'stairs': stairs,'paving_slabs': paving_slabs,
    'contacts':contacts , 'products': products})

def review(request):
    projects = LatestProducts.objects.get_products_for_main_page('ourproject')
    contacts = LatestProducts.objects.get_products_for_main_page('contact')
    return render(request, 'main/review.html', {'contacts':contacts, 'projects': projects })

def about(request):
    return render(request, 'main/about.html')


class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'tile' : Tile,
        'stair' : Stair
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    sluq_url_kwarg = 'slug'
