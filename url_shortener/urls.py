from django.conf.urls import patterns, include, url
from django.contrib import admin
from shorturls.views import LinkCreate

urlpatterns = patterns('',
	url(r'^$', LinkCreate.as_view(), name='home'),
)
