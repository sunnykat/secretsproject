from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.secret, name='index'),
    url(r'^/create$', views.create, name='create'),
    url(r'^/popular$', views.popular, name='popular'),
    url(r'^/delete/(?P<s_id>\d+)$', views.delete, name='delete'),
    url(r'^/like/(?P<s_id>\d+)$', views.like, name='like'),

]
