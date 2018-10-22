from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^$', views.orders_index, name = 'orders_index'),
    url(r'^manual/$', views.manual_order, name = 'manual_order'),
    url(r'^place_order/$', views.place_order, name = 'place_order'),
    url(r'^delete_order/(?P<pk>\d+)/$', views.delete_order, name = 'delete_order'),
]
