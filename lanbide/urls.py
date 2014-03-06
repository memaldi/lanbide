from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from paro import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lanbide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^municipio/([\w-]+)$', views.infoMunicipio),	
    url(r'^mapa', views.mapa),
    url(r'^provincias', views.provincias),
)
