from django.urls import path
from . import views 
from .views import *


urlpatterns = [
    path('', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail')
]

