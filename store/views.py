from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product


def index(request):
    '''

    :param request:
    :return:
    '''
    products = Product.objects.order_by('name')
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    products_per_page = paginator.get_page(page)

    context = {
        'products': products_per_page,
    }

    return render(request, 'index.html', context=context)


def search_products(request):
    products = Product.objects.order_by('name')

    if 'search' in request.GET:
        name_for_search = request.GET['search']
        products = products.filter(name__icontains=name_for_search)

    context: dict = {
        'products': products,
    }

    return render(request, 'search.html', context=context)