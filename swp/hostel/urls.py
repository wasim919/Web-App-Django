from django.conf.urls import url,include
from django.contrib import admin
from .import views

app_name = 'hostel'

#Add urls with approriate for leave message and complaint register

urlpatterns = [
    url(r'^$',views.hostel_dashboard, name = 'medical_dashboard'),
    #url(r'^leave_form$',views.leave_form, name = 'leave_form'),
    url(r'^leave_ack$',views.leave_ack, name = 'leave_ack'),
    url(r'^complaint_ack$',views.complaint_ack,name='complaint_ack'),
    #url(r'^sendmessage$',views.sendMessage, name = 'sendmessage'),
    #url(r'^applyleave$',views.applyLeave, name = 'applyLeave'),
]
