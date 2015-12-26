from django.conf.urls import patterns, url

urlpatterns = patterns(
	'emprendeespiritu.app.cursos.views',
	url(r'^$', 'get_all', name='vista_cursos_talleres'),
    url(r'^single/(?P<id>[0-9]+)/$', 'course_specific', name='vista_curso'),
    url(r'^comentario/(?P<curso>[0-9]+)/$', 'comentario_curso', name='vista_comentario_curso'),
    url(r'^like/(?P<curso>[0-9]+)/$', 'like_curso', name='like_curso'),
    url(r'^dislike/(?P<curso>[0-9]+)/$', 'dislike_curso', name='dislike_curso'),
    url(r'^suscribe/(?P<curso>[0-9]+)/$', 'request_curso', name='request_curso'),
	)