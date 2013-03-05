from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    #url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^$', 'newrelic_python_kata.views.home', name='home'),
    url(r'^query/$', 'query.views.index', name='query'),
    url(r'^name_filter/$', 'query.views.name_filter', name='name_filter'),

    # Examples:
    # url(r'^newrelic_python_kata/', include('newrelic_python_kata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
