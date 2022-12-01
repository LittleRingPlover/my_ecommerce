from django.shortcuts import render
from .models import Product


def show_all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/show_products.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
