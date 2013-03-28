from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$', 'webapp.views.api', name='api'),
    

    # Examples:
    # url(r'^$', 'foco_nutrition_api.views.home', name='home'),
    # url(r'^foco_nutrition_api/', include('foco_nutrition_api.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
