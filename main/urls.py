from django.conf.urls import patterns, include, url
from django.views.generic.edit import UpdateView

urlpatterns = patterns('',
                       url(r'^$',
                           'main.views.home',
                           name='home'),
                       url(r'^posts/(?P<id_post>\d+)/$',
                           'main.views.post',
                           name='post'),)
