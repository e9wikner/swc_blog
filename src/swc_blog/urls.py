from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url(r'^$', 'swc_blog.views.index', name='index'),

    url(r'^archive/$', 'swc_blog.views.archive', name='archive'),

    url(r'^about/$', 'swc_blog.views.about', name='about'),

    url((r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/'
         r'(?P<slug>[-\w]+)/$'), 'swc_blog.views.view_post',
        name='view-post'),
    )