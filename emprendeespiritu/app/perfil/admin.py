from django.contrib import admin

from emprendeespiritu.app.perfil.models import UserProfile, Pais, CursoSuscrito, TallerSuscrito

admin.site.register(Pais)
admin.site.register(UserProfile)
admin.site.register(CursoSuscrito)
admin.site.register(TallerSuscrito)