from django.conf.urls import patterns, url

urlpatterns = patterns(
	'emprendeespiritu.app.home.views',
    url(r'^$', 'index_view',name='vista_principal'),
    url(r'^home$', 'dashboard_view',name='vista_dashboard'),
	)