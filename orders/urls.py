from django.urls import path
from orders.views import OrderCreateView,CanceledTemplateView, SuccessTemplateView

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('success/', SuccessTemplateView.as_view(), name='order_success'),
    path('canceled/', CanceledTemplateView.as_view(), name='order_canceled'),
]
