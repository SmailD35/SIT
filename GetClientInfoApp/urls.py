from django.conf.urls import url

from . import views

app_name = 'get_client_info'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
