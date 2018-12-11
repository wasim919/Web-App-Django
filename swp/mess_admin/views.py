from django.shortcuts import render, redirect
from dashboard.models import MessAnnouncements
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from mess.models import MessLeave, MessRefund, OrderListMess, MessItems, MessFeedback
#from .forms import MessAnnouncementForm, AddAnnouncementForm
from django.http import HttpResponse
import datetime
import time
from django.template.loader import render_to_string
from orders.models import ManualOrder
from .forms import AddItemForm, AddAnnouncementForm, MessAnnouncementForm
from api_integration.models import Student
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from api_integration.models import Student
from dashboard.models import Messages

@login_required
def get_admin_status(request):
	st = 0
	dr = Student.objects.filter(student_first_name = str(request.user))
        if(len(dr) == 0):
            return 0
	print(dr, "ASDAS")
	if(dr[0].is_hostel_admin == True):
		st = 1
	elif(dr[0].is_mess_admin == True):
		st = 2
	elif(dr[0].is_medical_admin == True):
		st = 3
	return st


def check_isMessAdmin(request):
    return Student.objects.get(user=request.user).is_mess_admin
@login_required
def mess_admin_index(request):
    if(check_isMessAdmin(request)):
        return render(request, 'mess_admin/index.html')
    return render(request,'index.html')

@login_required
def mess_refund_accept(request, pk):
    if(check_isMessAdmin(request)):
        rt = MessRefund.objects.filter(pk = pk)
        temp = rt[0]
        temp.isDeleted = True
        temp.save()
        yt = Messages(message = ("Your mess refund request made on Date " + str(temp.timestamp) + " of rupees " +  str(temp.refund_amount) + " was accepted"), student = temp.student)
        yt.created_at = datetime.datetime.now().date()
        yt.modified_at = datetime.datetime.now().date()
        yt.modified_by = request.user
        yt.created_by = request.user
        yt.save()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')
@login_required
def mess_refund_reject(request, pk):
    if(check_isMessAdmin(request)):
        rt = MessRefund.objects.filter(pk = pk)
        temp = rt[0]
        temp.isDeleted = True
        temp.save()
        yt = Messages(message = ("Your mess refund request made on Date " + str(temp.timestamp) + " of rupees " +  str(temp.refund_amount) + " was rejected"), student = temp.student)
        yt.created_at = datetime.datetime.now().date()
        yt.modified_at = datetime.datetime.now().date()
        yt.modified_by = request.user
        yt.created_by = request.user
        yt.save()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')

@login_required
def mess_leave_accept(request, pk):
    if(check_isMessAdmin(request)):
        rt = MessLeave.objects.filter(pk = pk)
        temp = rt[0]
        temp.isDeleted = True
        print(temp.reason)
        temp.save()
        rp = MessLeave.objects.filter(pk = pk)
        print(rp[0].isDeleted)
        yt = Messages(message = ("Your mess leave request made on Date " + str(temp.timestamp) + " was accepted"), student = temp.student)
        yt.created_at = datetime.datetime.now().date()
        yt.modified_at = datetime.datetime.now().date()
        yt.modified_by = request.user
        yt.created_by = request.user
        yt.save()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')

@login_required
def mess_leave_reject(request, pk):
    if(check_isMessAdmin(request)):
        rt = MessLeave.objects.filter(pk = pk)
        temp = rt[0]
        temp.isDeleted = True
        temp.save()
        yt = Messages(message = ("Your mess leave request made on Date " + str(temp.timestamp)  + " was rejected"), student = temp.student)
        yt.created_at = datetime.datetime.now().date()
        yt.modified_at = datetime.datetime.now().date()
        yt.modified_by = request.user
        yt.created_by = request.user
        yt.save()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')

@login_required
def mess_admin_dashboard(request):
    if(check_isMessAdmin(request)):
        mess_announcements = list(MessAnnouncements.objects.filter(isDeleted = False))
        mess_announcements.sort(key = lambda a: a.timestamp, reverse = True)
        mess_leave = list(MessLeave.objects.filter(isDeleted = False))
        mess_leave.sort(key = lambda a: a.timestamp, reverse = True)
        mess_refund = list(MessRefund.objects.filter(isDeleted = False))
        mess_refund.sort(key = lambda a: a.timestamp, reverse = True)
        mess_items = list(MessItems.objects.filter(isDeleted = False))
        mess_items.sort(key = lambda a: a.timestamp, reverse = True)
        mess_order = list(OrderListMess.objects.filter(isDeleted = False))
        mess_order.sort(key = lambda a: a.timestamp, reverse = True)
        mess_feedback = list(MessFeedback.objects.filter(isDeleted = False))
        mess_feedback.sort(key = lambda a: a.timestamp, reverse = True)
        return render(request, 'mess_admin/mess_admin_dashboard.html', {'mess_announcements': mess_announcements,'mess_leave':mess_leave, 'mess_refund': mess_refund, 'mess_order': mess_order, 'mess_items': mess_items,'admin_status': get_admin_status(request),
        'mess_feedback': mess_feedback,
        'mr': len(mess_refund),
        'ml': len(mess_leave),
        'mo': len(mess_order)
        })
    return render(request,'index.html')
@login_required
def mess_leave_show(request, pk):
    if(check_isMessAdmin(request)):
        leave = get_object_or_404(MessLeave, pk = pk)
        return render(request, 'mess_admin/leaves.html', {'pk': pk, 'leave': leave, 'admin_status': get_admin_status(request)})
    return render(request,'index.html')
@login_required
def mess_refund_show(request, pk):
    if(check_isMessAdmin(request)):
        refund = get_object_or_404(MessRefund, pk = pk)
        return render(request, 'mess_admin/refunds.html', {'pk': pk, 'refund': refund, 'admin_status': get_admin_status(request)})
    return render(request,'index.html')


# announcement_title=forms.CharField(label='announcement_title',widget=forms.TextInput(attrs={"class":"form-control"}))
# announcement=forms.CharField(label='announcement',widget=forms.TextInput(attrs={"class":"form-control"}))
# timestamp=forms.DateField(label='timestamp',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_at=timestamp=forms.DateField(label='created_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_by=forms.CharField(label='created_by',widget=forms.TextInput(attrs={"class":"form-control"}))
# modified_at=timestamp=forms.DateField(label='modified_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# modified_by=forms.CharField(label='modified_by',widget=forms.TextInput(attrs={"class":"form-control"}))
@login_required
def announcement_delete(request, id):
    if(check_isMessAdmin(request)):
        print(id)
        announcement = MessAnnouncements.objects.get(pk=id)
        announcement.delete()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')
@login_required
def leave_delete(request, id):
    if(check_isMessAdmin(request)):
        leave = MessLeave.objects.get(pk=id)
        leave.delete()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')
@login_required
def refund_delete(request, id):
    if(check_isMessAdmin(request)):
        refund = MessRefund.objects.get(pk=id)
        refund.isDeleted = True
        refund.save()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')

@login_required
def item_delete(request, id):
    if(check_isMessAdmin(request)):
        item = MessItems.objects.get(pk = id)
        item.isDeleted = True
        item.save()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')

@login_required
def order_delete(request, id):
    if(check_isMessAdmin(request)):
        order = OrderListMess.objects.get(pk = id)
        order.isDeleted = True
        order.save()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')

@login_required
def feedback_delete(request, id):
    if(check_isMessAdmin(request)):
        feedback = MessFeedback.objects.get(pk = id)
        feedback.isDeleted = True
        feedback.save()
        return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')

@login_required
def announcement_edit(request, id):
    if(check_isMessAdmin(request)):
        Mess_announcement = MessAnnouncements.objects.get(pk=id)
        Mess_announcement_form = AddAnnouncementForm(initial = {
        'announcement_title': Mess_announcement.announcement_title,
        'announcement': Mess_announcement.announcement,
        'admin_status': get_admin_status(request)
        })
        print(Mess_announcement_form)
        return render(request, 'mess_admin/edit_announcements.html', {
        'form': Mess_announcement_form,
        'id': id,
        'admin_status': get_admin_status(request)
        })
    return render(request,'index.html')
@login_required
def item_edit(request, id):
    if(check_isMessAdmin(request)):
        Mess_item = MessItems.objects.get(pk=id)
        Mess_item_form = AddItemForm(initial = {
        'item_name': Mess_item.item_name,
        'quantity': Mess_item.quantity,
        'cost': Mess_item.cost,
        'admin_status': get_admin_status(request)
        })
        #print(Mess_announcement_form)
        return render(request, 'mess_admin/edit_items.html', {
        'form': Mess_item_form,
        'id': id,
        'admin_status': get_admin_status(request)
        })
    return render(request,'index.html')
@login_required
def add_announcement(request):
    if(check_isMessAdmin(request)):
        if request.method == 'GET':
            add_announcement_form = AddAnnouncementForm()
            return HttpResponse(render_to_string('mess_admin/add.html',context={
            'add_announcement_form': add_announcement_form,
            'admin_status': get_admin_status(request)
            }))
    return render(request,'index.html')
@login_required
def add_item(request):
    if(check_isMessAdmin(request)):
        if request.method == 'GET':
            add_item_form = AddItemForm()
            return HttpResponse(render_to_string('mess_admin/addI.html',context={'add_item_form': add_item_form, 'admin_status': get_admin_status(request)}))
    return render(request,'index.html')
@login_required
def add_announcement_url(request):
    if(check_isMessAdmin(request)):
        if request.method == 'POST':
            form = AddAnnouncementForm(request.POST)
            if form.is_valid():
                add_announcement_form=form.save(commit=False)
                add_announcement_form.timestamp=datetime.datetime.now()
                add_announcement_form.created_at=datetime.datetime.now().date()
                add_announcement_form.modified_at = datetime.datetime.now().date()
                add_announcement_form.created_by=request.user.username
                add_announcement_form.modified_by=request.user.username
                add_announcement_form.save()

                return redirect('mess_admin:mess_admin_dashboard')
        print(form.errors)
    return render(request,'index.html')
@login_required
def add_item_url(request):
    if(check_isMessAdmin(request)):
        if request.method == 'POST':
            form = AddItemForm(request.POST)
            if form.is_valid():
                add_item_form=form.save(commit=False)
                add_item_form.timestamp=datetime.datetime.now()
                add_item_form.created_at=datetime.datetime.now().date()
                add_item_form.modified_at = datetime.datetime.now().date()
                add_item_form.created_by=request.user.username
                add_item_form.modified_by=request.user.username
                add_item_form.save()
                return redirect('mess_admin:mess_admin_dashboard')
    return render(request,'index.html')
@login_required
def save_edit_changes(request, id):
    if(check_isMessAdmin(request)):
        if request.method == 'POST':
            try:
                announcement = MessAnnouncements.objects.get(pk=id)
            except MessAnnouncements.DoesNotExist:
                announcement = None
            if announcement is not None:
                announcement_title = request.POST.get('announcement_title')
                announcement_body = request.POST.get('announcement')
                flag = 0
                if announcement_title != announcement.announcement_title:
                    announcement.announcement_title = announcement_title
                    flag = 1
                    announcement.announcement = announcement_body
                    announcement.timestamp=datetime.datetime.now()
                    announcement.modified_at = datetime.datetime.now().date()
                    announcement.modified_by=request.user.username
                if announcement_body != announcement.announcement:
                    announcement.announcement = announcement_body
                    if flag == 0:
                        announcement.timestamp=datetime.datetime.now()
                        announcement.modified_at = datetime.datetime.now().date()
                        announcement.modified_by=request.user.username
                announcement.save()
            return redirect('mess_admin:mess_admin_dashboard')
        print(request.method)
    return render(request,'index.html')
@login_required
def save_item_changes(request, id):
    if(check_isMessAdmin(request)):
        if request.method == 'POST':
            try:
                Item = MessItems.objects.get(pk=id)
            except MessItems.DoesNotExist:
                Item = None
            if Item is not None:
                Item_name = request.POST.get('item_name')
                Item_quantity = request.POST.get('quantity')
                Item_cost = request.POST.get('cost')
                flag = 0
                if Item_name != Item.item_name or Item_quantity != Item.quantity or Item_cost != Item.cost:
                    Item.item_name = Item_name
                    Item.quantity = Item_quantity
                    Item.cost = Item_cost
                    Item.timestamp=datetime.datetime.now()
                    Item.modified_at = datetime.datetime.now().date()
                    Item.modified_by=request.user.username
                    Item.save()
                    print("THE FORM WAS SAVED")
            return redirect('mess_admin:mess_admin_dashboard')
        print(request.method)
        print("HERE")
    return render(request,'index.html')
"""
def manual_orders(request):
    manual_orders = ManualOrder.objects.all()
    length = len(manual_orders)
    return HttpResponse(render_to_string('Mess_admin/manual_order.html',context={
    'manual_orders': manual_orders,
    'len': length,
    }))

def add_item(request):
    if request.method == 'POST':
        add_item_form = AddItemForm(data = request.POST)
        if add_item_form.is_valid():
            form = add_item_form.save(commit = False)
            form.item_type = 'Others'
            form.timestamp=datetime.datetime.now()
            form.created_at = datetime.datetime.now().date()
            # print(form.created_at)
            # print('hi')
            form.modified_at = datetime.datetime.now().date()
            form.modified_by = request.user.username
            form.created_by = request.user.username
            print('hi')
            form.save()
            print('done')
        return redirect('Mess_admin:Mess_admin_dashboard')
    else:
        item_form = AddItemForm()
        return HttpResponse(render_to_string('Mess_admin/item_form.html',context={
        'form': item_form,
        }))
"""
