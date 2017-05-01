from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /schooltrack/
    url(r'^$', views.index, name='index'),
    # ex: /schooltrack/1480/
    #url(r'^(?P<school_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^filter/(?P<district_filter>\w{1,50})/$', views.filter, name='filter'),
	]
