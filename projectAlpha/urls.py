from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectAlpha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',"student.views.index"),
    url(r'^home/',"student.views.home"),
    url(r'^addstudent/',"student.views.addstudent"),
    url(r'^register/',"student.views.register"),
    url(r'^search/',"student.views.search"),
    url(r'^searchStudent/',"student.views.searchStudent"),
)
