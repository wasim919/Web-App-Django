from django.contrib import admin
from .models import OrderList, OrderHistory, Items, ManualOrder

admin.site.register(OrderList)
admin.site.register(OrderHistory)
admin.site.register(Items)
admin.site.register(ManualOrder)
