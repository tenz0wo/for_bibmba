from django.shortcuts import render
from .models import Products, Home_content, Home_Slider

def index(request):
    array = ['1', '2', '3', '4', '5', '6', '7', '8']
    product = Products.objects.all()
    home = Home_content.objects.all()
    slider = Home_Slider.objects.all()
    context = {
        "product": product, 
        "home": home,
        "slider": slider,
        "array": array,
        }
    return render(request, 'main/index.html', context)
    
def cart(request):
    return render(request, 'main/cart.html')

def categories(request):
    product = Products.objects.all()
    context = {
        "product": product, 
        }
    return render(request, 'main/categories.html', context)

def checkout(request):
    return render(request, 'main/checkout.html')
