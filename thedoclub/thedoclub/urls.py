from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'homepage.views.home', name='home'),
    url(r'^event/attend', 'event.views.attend', name='attend'),
    url(r'^presentation/choose/(?P<repo_id>\w+)?', 'presentation.views.choose_confirm', name='presentation-choose-confirm'),
    url(r'^presentation/choose/?', 'presentation.views.choose', name='presentation-choose'),
    url(r'^presentation/(?P<repo_id>\w+)/edit/?', 'presentation.views.edit', name='presentation-edit'),
    url(r'^presentation/(?P<repo_id>\w+)/?', 'presentation.views.view', name='presentation-view'),
    url(r'^oauth/authorize/?', 'oauth.views.authorize', name='oauth-authorize'),
    url(r'^oauth/callback/?', 'oauth.views.callback', name='oauth-callback'),
    url(r'^oauth/start/?', 'oauth.views.start', name='oauth-start'),
    url(r'^oauth/end/?', 'oauth.views.end', name='oauth-end'),
    url(r'^oauth/status/?', 'oauth.views.status', name='oauth-status'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()