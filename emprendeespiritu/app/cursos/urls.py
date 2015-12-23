from django.conf.urls import patterns, url

urlpatterns = patterns(
	'emprendeespiritu.app.cursos.views',
    url(r'^single/$', 'course_specific', name='vista_curso'),
	)