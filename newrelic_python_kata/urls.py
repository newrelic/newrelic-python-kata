from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    #url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^$', 'newrelic_python_kata.views.home', name='home'),
    url(r'^kata1/$', 'employees.views.list', name='list'),
    url(r'^kata2/$', 'employees.views.filtering', name='query'),
    url(r'^kata3/$', 'factorial.views.factorial_h', name='factorial'),
    url(r'^kata4/$', 'weather.views.weather', name='weather'),

    # Examples:
    # url(r'^newrelic_python_kata/', include('newrelic_python_kata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
            )
