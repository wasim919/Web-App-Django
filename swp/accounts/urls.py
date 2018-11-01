from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.student_login, name = 'student_login'),
    url(r'^student_logout/$', views.user_logout, name = "student_logout")
]
