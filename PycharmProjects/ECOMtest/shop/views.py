from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from shop.models import Product


def index(request):
    product_object = Product.objects.all()
    items_name = request.GET.get("items-name")
    if items_name != "" and items_name is not None:
        product_object = Product.objects.filter(title__icontains=items_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get("page")
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})


def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})