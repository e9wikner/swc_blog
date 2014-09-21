from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url(r'^$', 'blog.views.index', name='index'),

    url(r'^archive/$', 'blog.views.archive', name='archive'),

    url(r'^about/$', 'blog.views.about', name='about'),

    url((r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/'
         r'(?P<slug>[-\w]+)/$'), 'blog.views.view_post', name='blog-view-post'),
    )