from django.conf.urls import url
from . import views

app_name = 'api_integration'

urlpatterns = [
    url(r'^(?P<token>.*)/', views.callback, name = 'callback'),
]
