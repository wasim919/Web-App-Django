from django.conf.urls import url
from . import views

app_name = 'mess_admin'

urlpatterns = [
    url(r'^$', views.mess_admin_index, name = 'mess_admin_index'),
   	url(r'^mess_admin_dashboard', views.mess_admin_dashboard, name = 'mess_admin_dashboard'),
	url(r'^announcement_delete/(?P<id>\d+)', views.announcement_delete, name = 'announcement_delete'),
	url(r'^item_delete/(?P<id>\d+)', views.item_delete, name = 'item_delete'),
	url(r'^leave_delete/(?P<id>\d+)', views.leave_delete, name = 'leave_delete'),
	url(r'^refund_delete/(?P<id>\d+)', views.refund_delete, name = 'refund_delete'),
	url(r'^order_delete/(?P<id>\d+)', views.order_delete, name = 'order_delete'),
	url(r'^add_announcement/', views.add_announcement, name='add_announcement'),
	url(r'^add_item/', views.add_item, name='add_item'),
	url(r'^announcement_edit/(?P<id>\d+)/$', views.announcement_edit, name = 'announcement_edit'),
	url(r'^item_edit/(?P<id>\d+)/$', views.item_edit, name = 'item_edit'),
	url(r'^add_announcement_url/', views.add_announcement_url, name='add_announcement_url'),
	url(r'^add_item_url/', views.add_item_url, name='add_item_url'),
	url(r'^show_leave/(?P<pk>\d+)', views.mess_leave_show, name="show_leave"),
	url(r'^show_refund/(?P<pk>\d+)', views.mess_refund_show, name="show_refund"),	
	url(r'^save_edit_changes/(?P<id>\d+)/$', views.save_edit_changes, name = 'save_edit_changes'),
	url(r'^save_item_changes/(?P<id>\d+)/$', views.save_item_changes, name = 'save_item_changes'),
	url(r'^add_item/', views.mess_admin_dashboard, name='add_item')
]	
