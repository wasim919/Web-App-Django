from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ManualOrderForm
from  accounts.models import Student
from .models import Items, OrderList
import datetime
import time

@login_required
def orders_index(request):
    items = list(Items.objects.all())
    if items:

        books = list(filter(lambda x: x.item_type == "Book", items))
        stationary = list(filter(lambda x: x.item_type == "Stationary", items))
        others = list(filter(lambda x: x.item_type == "Others", items))

        all_orders = list(OrderList.objects.all())
        user_orders = list(filter(lambda x: x.student.user == request.user, all_orders))
        return render(request, 'orders/orders_index.html', {
            'books': books,
            'stationary': stationary,
            'others': others,
            'items': items,
            'user_orders': user_orders
        })
    else:
        return render(request, 'orders/orders_index.html', {
            'items': items,
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

def dot(K, L):
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))



def changeQuantity(items_p, items_posted):
    j = 0
    for i in range(len(items_posted)):
        if int(items_posted[i]) > 0:
            obj = Items.objects.get(item_name=items_p[j].item_name)
            j+=1
            obj.quantity = obj.quantity - int(items_posted[i])
            obj.save()

def store_in_items_list(student, items_purchased, items_post, creator):
    print('hello')
    print(items_post)
    print(items_purchased)
    j = 0
    for i in range(len(items_post)):
        if int(items_post[i]) != 0:
            obj = OrderList.objects.create(student=student, item=items_purchased[j], quantity=int(items_post[i]))
            obj.created_at=obj.timestamp
            obj.created_by=creator.username
            obj.save()
            j += 1

@login_required
def place_order(request):
    if request.method == 'POST':
        items = list(Items.objects.all())

        books = list(filter(lambda x: x.item_type == "Book", items))
        stationary = list(filter(lambda x: x.item_type == "Stationary", items))
        others = list(filter(lambda x: x.item_type == "Others", items))

        books_post = request.POST.getlist('books')
        stationary_post = request.POST.getlist('stationary')
        others_post = request.POST.getlist('others')


        books_cost = 0
        stationary_cost = 0
        others_cost = 0
        if books_post:
            books_cost = dot([a.cost for a in books], list(map(int, books_post)))
        if stationary_post:
            stationary_cost = dot([a.cost for a in stationary], list(map(int, stationary_post)))
        if others_post:
            others_cost = dot([a.cost for a in others], list(map(int, others_post)))

        total_cost = books_cost + stationary_cost + others_cost

        if books:
            books_purchased = [books[i] for i in range(len(books)) if books_post[i]!='0']
        if stationary:
            stationary_purchased = [stationary[i] for i in range(len(stationary)) if stationary_post[i]!='0']
        if others:
            others_purchased = [others[i] for i in range(len(others)) if others_post[i]!='0']

        if books_post:
            student = Student.objects.get(user=request.user)
            store_in_items_list(student, books_purchased, books_post, request.user)
            changeQuantity(books_purchased, books_post)

        print(stationary_purchased)
        if stationary_post:
            student = Student.objects.get(user=request.user)
            store_in_items_list(student, stationary_purchased, stationary_post, request.user)
            changeQuantity(stationary_purchased, stationary_post)


        if others_post:
            student = Student.objects.get(user=request.user)
            store_in_items_list(student, others_purchased, others_post, request.user)
            changeQuantity(others_purchased, others_post)

        return redirect('orders:orders_index')
