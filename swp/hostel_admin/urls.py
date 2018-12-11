from django.conf.urls import url
from . import views

app_name = 'hostel_admin'

urlpatterns = [
    url(r'^$', views.hostel_admin_index, name = 'hostel_admin_index'),
    url(r'^hostel_admin_dashboard/$', views.hostel_admin_dashboard, name = 'hostel_admin_dashboard'),
    url(r'^announcement_delete/(?P<id>\d+)/$', views.announcement_delete, name = 'announcement_delete'),
    url(r'^announcement_edit/(?P<id>\d+)/$', views.announcement_edit, name = 'announcement_edit'),
    url(r'^add_announcement/$', views.add_announcement, name = 'add_announcement'),
    url(r'^add_announcement_url/$', views.add_announcement_url, name = 'add_announcement_url'),
    url(r'^save_edit_changes/(?P<id>\d+)/$', views.save_edit_changes, name = 'save_edit_changes'),
    url(r'^manual_orders/$', views.manual_orders, name = 'manual_orders'),
    url(r'^complaint_details/(?P<id>\d+)/$', views.complaint_details, name = 'complaint_details'),
    url(r'^hostel_leaves/$', views.hostel_leaves, name = 'hostel_leaves'),
    url(r'^hostel_complaints/$', views.hostel_complaints, name = 'complaints'),
    url(r'^hostel_leave_accept/(?P<id>\d+)/$', views.hostel_leave_accept, name = 'hostel_leave_accept'),
    url(r'^hostel_leave_reject/(?P<id>\d+)/$', views.hostel_leave_reject, name = 'hostel_leave_reject'),
    url(r'^add_item/$', views.add_item, name = 'add_item'),
    url(r'^add_courier/$', views.add_courier, name = 'add_courier'),
    url(r'^add_student_courrier/$', views.add_student_courrier, name = 'add_student_courrier'),
    url(r'^add_selfhelp/$', views.add_selfhelp, name = 'add_selfhelp'),
    url(r'^add_selfhelp_view/$', views.add_selfhelp_view, name = 'add_selfhelp_view'),
]
