from django.conf.urls import patterns, url
from polls.views import detail, results, vote

urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results', name='presults'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
