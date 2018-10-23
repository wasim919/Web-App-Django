from django.conf.urls import url, include
from django.contrib import admin
from .import views

app_name = 'medical'

urlpatterns = [
    url(r'^$',views.medical_dashboard, name = 'medical_dashboard'),
    url(r'^medical_message$',views.medical_message, name = 'medical_message'),
    url(r'^medical_leave$',views.medical_leave, name = 'medical_leave'),
    url(r'^sendmessage$',views.sendMessage, name = 'sendmessage'),
    url(r'^applyleave$',views.applyLeave, name = 'applyLeave'),
]
