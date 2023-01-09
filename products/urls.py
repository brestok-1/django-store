from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    path('', ProductsView.as_view(), name='index'),
    path('category/<int:category_id>', ProductsCategoryView.as_view(), name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
