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
]
