from django.conf.urls import patterns, url
from django.contrib.auth.decorators import permission_required
from emprendeespiritu.app.home.views import dashboard_view

urlpatterns = patterns(
	'emprendeespiritu.app.home.views',
	url(r'^$', 'login_view',name='vista_index'),
    url(r'^accounts/login/$', 'index_view',name='vista_principal'),
    url(r'^home$', (permission_required('dashboard_view'))(dashboard_view),name='vista_dashboard'),
    url(r'^send_mail', 'send_mail_view', name="vista_email"),
    url(r'^logout$', 'logout_view', name='vista_logout'),
	)