from django.conf.urls import *

urlpatterns = patterns('coderbits.views',
  url(r'^new$', 'new', name='snippet_new'),
  url(r'^show/(?P<snippet_id>\d+)/$', 'show', name='snippet_show'),
)
