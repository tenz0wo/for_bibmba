from django.shortcuts import render, redirect
from .models import Products, Home_content, Home_Slider
from .forms import SubForm

def index(request):
    array = ['1', '2', '3', '4', '5', '6', '7', '8']
    product = Products.objects.all()
    home = Home_content.objects.all()
    slider = Home_Slider.objects.all()
   
    error = ''
    if request.method == "POST":
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена некоректно'

    form = SubForm()
    context = {
            "product": product, 
            "home": home,
            "slider": slider,
            "array": array,
            'form': form,
            'error': error
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
