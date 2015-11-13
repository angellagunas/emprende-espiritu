from django.contrib import admin

from emprendeespiritu.app.perfil.models import UserProfile, Pais

admin.site.register(Pais)
admin.site.register(UserProfile)