from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='index'),
    url(r'^main', views.main, name='index'),
]