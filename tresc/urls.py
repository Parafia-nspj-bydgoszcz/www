from django.conf.urls.defaults import *
from tresc.views import *

urlpatterns = patterns('',
#   url(r'^$', main, ),
    url(r'(?P<odnosnik>[w\w\-_]+)/$', index, ),
)
