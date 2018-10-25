from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'mess'

#Add urls with approriate for leave message and complaint register

urlpatterns = [
    url(r'^$',views.mess_dashboard, name = 'mess_dashboard'),
    url(r'^leave_form$',views.leave_form, name = 'leave_form'),
    url(r'^mess_leave$',views.mess_leave, name = 'mess_leave'),
	url(r'refund_form$',views.refund_form, name = 'refund_form'),
    url(r'^applyMessRefund$',views.applyMessRefund, name = 'applyMessRefund'),
	url(r'^feedback_form$',views.feedback_form, name = 'feedback_form'),
    url(r'^submit_feedback$',views.submit_feedback, name = 'submit_feedback'),
]

if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
