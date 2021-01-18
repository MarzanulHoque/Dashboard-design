from django.shortcuts import render, redirect

from django.views import View

from store.models.customer import Customer
from store.models.product import Product
from store.middlewares.auth import auth_middleware
from store.models.orders import Order


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_order_by_customer(customer)

        return render(request, 'orders.html', {'orders': orders})
