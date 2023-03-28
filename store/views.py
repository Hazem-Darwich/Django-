from django.shortcuts import render
from django.views import View
from .models import Product , Category


def home(request): 
    products = Product.objects.all()
    return render(request=request, template_name=r"store\home.html",context={"products":products , })


def product_detail(requset , slug):
    product = Product.objects.get(slug = slug)

    return render(request=requset , template_name="store/product_detail.html", context={"product" : product})
    