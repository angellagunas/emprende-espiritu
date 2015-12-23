from django.conf.urls import patterns, url

urlpatterns = patterns(
	'emprendeespiritu.app.talleres.views',
    url(r'^single/(?P<id>[0-9]+)/$', 'taller_specific', name='vista_taller'),
    url(r'^comentario/(?P<taller>[0-9]+)/$', 'comentario_taller', name='vista_comentario_taller'),
    url(r'^like/(?P<taller>[0-9]+)/$', 'like_taller', name='like_taller'),
    url(r'^dislike/(?P<taller>[0-9]+)/$', 'dislike_taller', name='dislike_taller'),
	)