from django.views.generic.list import ListView
from django.views.generic import View
from django.http import JsonResponse

from shop.models import Product, Order


class ProductListAPI(View):

    def get(self, request):
        products = {
            product.id: {
                'price': product.price,
                'name': product.name,
                'image': product.image_url,
            }
            for product in Product.objects.all()
        }
        return JsonResponse(products)


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        total_price = 0
        for product in context['product_list']:
            total_price += product.price
        context['total_price'] = total_price

        return context


class OrderListAPI(View):

    def get(self, request):
        orders = {
            order.id: {
                'order_positions': {
                    order_position.id: {
                        'total_price': order_position.total_price,
                        'product_name': order_position.product.name,
                        'quantity': order_position.quantity,
                    }
                    for order_position in order.orderposition_set.all()
                },
                'address': order.address,
            }
            for order in Order.objects.filter(user=request.user)
        }
        return JsonResponse(orders)
