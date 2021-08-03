from django.urls import path
from . import views
from .views import ProductDetailsView


urlpatterns = [
    path('', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailsView.as_view(), name='product_detail')
]
