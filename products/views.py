from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import *
from users.models import User


# Create your views here.
def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


class ProductsView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['title'] = 'Store'
        context['category'] = ProductCategory.objects.all()
        return context

# def products(request):
#     context = {
#         'title': 'Store - Catalog',
#         'products': Product.objects.all(),
#         'category': ProductCategory.objects.all(),
#     }
#     return render(request, 'products/products.html', context)


class ProductsCategoryView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsCategoryView, self).get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.all()
        context['title'] = 'Store-Catalog'
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id'])


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(
        request.META['HTTP_REFERER'])  # we define on what page user is and redirect to this page


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META['HTTP_REFERER'])
