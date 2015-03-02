from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required

from shop.views import ProductListView, OrderListAPI, ProductListAPI

urlpatterns = patterns(
    '',
    url(r'^products/', ProductListView.as_view()),
    url(r'^api/products/', ProductListAPI.as_view()),
    url(r'^api/orders/', login_required(OrderListAPI.as_view())),
)
