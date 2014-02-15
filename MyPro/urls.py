from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'PyBugs.views.index'),
    url(r'^login/$', 'PyBugs.views.login'),
    url(r'^account/$', 'PyBugs.views.account' ,name='account'),
    url(r'^create_project/$', 'PyBugs.views.create_project' ,name='create_project'),
    url(r'^new_bug/$', 'PyBugs.views.new_bug',name='new_bug'),
    url(r'^edit_bug/(?P<pk>\d+)/$', 'PyBugs.views.edit_bug',name='edit_bug'),
    url(r'^del_bug/(?P<pk>\d+)/$', 'PyBugs.views.del_bug'),
    url(r'^edit_developer/(?P<pk>\d+)/$', 'PyBugs.views.edit_developer',name='edit_developer'),
     url(r'^new_developer/$', 'PyBugs.views.create_developer',name='new_developer'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/index/'}),
)
