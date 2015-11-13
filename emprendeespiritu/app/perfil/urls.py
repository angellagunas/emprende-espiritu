from django.conf.urls import patterns, url

urlpatterns = patterns(
	'emprendeespiritu.app.perfil.views',
    url(r'^$', 'index_view',name='vista_principal'),
	)