from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product


def index(request):
    products = Product.objects.order_by('name')
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    products_per_page = paginator.get_page(page)

    context = {
        'products': products,
    }

    return render(request, 'index.html', context=context)
