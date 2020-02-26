
from django.conf.urls import url
from App16 import views

# TEMPLATE TAGGING
app_name = 'Pro16'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
