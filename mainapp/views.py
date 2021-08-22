from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import DetailView

from .models import *
from .mixins import ContactDetailMixin

def index(request):
    products = LatestProducts.objects.get_products_for_main_page('tile', 'stair', 'pavingslab', 'pavingstone')
    tiles = LatestProducts.objects.get_products_for_main_page('tile')
    stairs = LatestProducts.objects.get_products_for_main_page('stair')
    paving_slabs = LatestProducts.objects.get_products_for_main_page('pavingslab')
    paving_stones = LatestProducts.objects.get_products_for_main_page('pavingstone')
    contacts = Contact.objects.all()
    return render(request, 'main/index.html',
     {'tiles': tiles, 'stairs': stairs,'paving_slabs': paving_slabs, 'paving_stones' : paving_stones, 
    'contacts':contacts , 'products': products})

def review(request):
    projects = OurProject.objects.all()
    contacts = Contact.objects.all()
    return render(request, 'main/review.html', {'contacts':contacts, 'projects': projects })

def about(request):
    contacts = Contact.objects.all()
    return render(request, 'main/about.html', {'contacts':contacts})
    

class ProductDetailView(ContactDetailMixin, DetailView):

    CT_MODEL_MODEL_CLASS = {
        'tile' : Tile,
        'stair' : Stair,
        'pavingslab' : PavingSlab,
        'pavingstone': PavingStone
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    sluq_url_kwarg = 'slug'