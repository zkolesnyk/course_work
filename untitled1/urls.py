from django.conf.urls import url, patterns, static
from django.contrib import admin
from coursework.views import *
from django.conf import settings

urlpatterns = patterns('fb-41.com.ua',
    url(r'^auth/login/$', login),
    url(r'^auth/logout/$', logout),
    url(r'^auth/register/$', register),
    url(r'^$', home, name='home'),
    url(r'^admin', admin.site.urls),
    url(r'^group-list/', group_list),
    url(r'^schedule/', schedule),
    url(r'^upload/', upload),
    # url(r'^download/(?P<path>.*)$', 'serve', {'document_root': MEDIA_ROOT}),
    url(r'^study-materials', study_materials)
)

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
