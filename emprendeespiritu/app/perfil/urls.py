from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required
from emprendeespiritu.app.home.views import dashboard_view

urlpatterns = patterns(
	'emprendeespiritu.app.perfil.views',
    url(r'^$', 'perfil_view', name="vista_perfil"),
	)