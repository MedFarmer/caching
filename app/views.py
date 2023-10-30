from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.core.cache import cache
from django.views.generic import ListView
from .models import *


class ListProducts(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'list_products.html'
    
    def get_queryset(self):
        
        products = cache.get('products')
        
        if products is None:
            products = Product.objects.all()
            cache.set('products', products, 300)
            
        return products
