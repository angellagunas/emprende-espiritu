from django.conf.urls import patterns, url

urlpatterns = patterns(
	'emprendeespiritu.app.blog.views',
    url(r'^$', 'blog_view', name='vista_blog'),
    url(r'^single/$', 'blog_specific', name='vista_entrada'),
	)