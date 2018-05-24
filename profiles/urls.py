from django.conf.urls import url
from . import views

app_name='nagios'
urlpatterns = [
    url(r'^registration$',  views.update_profile, name='Update profiles'),
    ]