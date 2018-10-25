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
    url(r'^applyMessLeave$',views.applyMessLeave, name = 'applyMess	Leave'),
    url(r'^leave-ack$',views.leave_ack,name='complaint_ack'),
	url(r'refund_form$',views.leave_form, name = 'refund_form'),
    url(r'^applyMessRefund$',views.applyMessRefund, name = 'applyMessRefund'),
    url(r'^refund-ack$',views.leave_ack,name='refund_ack'),
	url(r'^feedback_form$',views.leave_form, name = 'feedback_form'),
    url(r'^submit_feedback$',views.submit_feedback, name = 'submit_feedback'),
    url(r'^feedback-ack$',views.feedback_ack,name='feedback_ack'),
]

if settings.DEBUG: 
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
