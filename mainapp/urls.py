from django.conf.urls import url
from django.urls import path
from . import views 
from .views import *


urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'about-us', views.about, name="about"),
    url(r'review', views.review, name="review"),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail')
]
