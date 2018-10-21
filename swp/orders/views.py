from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import ManualOrderForm
from .models import Items

@login_required
def orders_index(request):
    items = get_list_or_404(Items, )

    books = list(filter(lambda x: x.item_type == "Book", items))

    stationary = list(filter(lambda x: x.item_type == "Stationary", items))

    others = list(filter(lambda x: x.item_type == "Others", items))

    return render(request, 'orders/orders_index.html', {
        'books': books,
        'stationary': stationary,
        'others': others
    })

@login_required
def manual_order(request):
    if request.method == 'POST':
        manual_order = ManualOrderForm(request.POST)
        if manual_order.is_valid():
            manual_order.save()
            return render(request, 'orders/manual_placed.html', {
                'order_name': request.POST.get('order_name'),
                'order_type': request.POST.get('order_type')
            })
        else:
            return render(request, 'orders/manual_order.html', {
            'form': manual_order
            })
    else:
        manual_order = ManualOrderForm()
        return render(request, 'orders/manual_order.html', {
        'form': manual_order
        })

@login_required
def place_order(request):
    if request.method == 'POST':
        items = get_list_or_404(Items, )

        books = list(filter(lambda x: x.item_type == "Book", items))

        stationary = list(filter(lambda x: x.item_type == "Stationary", items))

        others = list(filter(lambda x: x.item_type == "Others", items))
        print(request.POST)
        print(request.POST.get("others"))
        ordered_books_length = request.POST.get('books')
        print(ordered_books_length)
        return render(request, 'orders/order_placed.html')
