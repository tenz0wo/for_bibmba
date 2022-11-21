from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('cart', views.cart, name='cart'),
    path('catalog', views.categories, name='catalog'),
    path('checkout', views.checkout, name='checkout'),

]