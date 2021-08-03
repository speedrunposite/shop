from django.urls import path
from . import views
<<<<<<< HEAD
=======
from .views import *
>>>>>>> 772022faf32c447908057b0b14ae8a029dfc4e12


urlpatterns = [
    path('', views.index, name="home"),
<<<<<<< HEAD
    path('about-us', views.about, name="about")
=======
    path('about-us', views.about, name="about"),
    # path('products/<str:slug>/<str:slug>/', ProductDetailsView.as_view(), name='product_detail')
>>>>>>> 772022faf32c447908057b0b14ae8a029dfc4e12
]
