from django import forms
from .models import ManualOrder, Items, OrderList, OrderHistory

class ManualOrderForm(forms.ModelForm):
    class Meta:
        model = ManualOrder
        fields = (
            'order_type',
            'order_name',
        )
