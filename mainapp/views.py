from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Tile

def index(request):
    # тут вернем шаблон
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

class ProductDetailsView(DetailView):
    #словарь для продуктов

    CT_MODEL_CLASS={
        'tiles': Tile   
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_CLASS[kwargs.get('ct_model')]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    content_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwargs = 'slug'
