from django.conf.urls import url
from . import views

app_name = 'medical_admin'

urlpatterns = [
    url(r'^$', views.medical_admin_index, name = 'medical_admin_index'),
    url(r'^medical_admin_dashboard/$', views.medical_admin_dashboard, name = 'medical_admin_dashboard'),
    url(r'^medical_announcement_delete/(?P<id>\d+)/$', views.medical_announcement_delete, name = 'medical_announcement_delete'),
    url(r'^medical_announcement_edit/(?P<id>\d+)/$', views.medical_announcement_edit, name = 'medical_announcement_edit'),
    url(r'^medical_add_announcement/$', views.medical_add_announcement, name = 'medical_add_announcement'),
    url(r'^medical_add_announcement_url/$', views.medical_add_announcement_url, name = 'medical_add_announcement_url'),
    url(r'^medical_save_edit_changes/(?P<id>\d+)/$', views.medical_save_edit_changes, name = 'medical_save_edit_changes'),
    url(r'^medical_leave_details/(?P<id>\d+)/$', views.medical_leave_details, name = 'medical_leave_details'),
]
