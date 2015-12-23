from django.contrib import admin

from emprendeespiritu.app.talleres.models import Taller, SemanaTaller, ArchivoSemana, ComentarioTaller

admin.site.register(Taller)
admin.site.register(SemanaTaller)
admin.site.register(ArchivoSemana)
admin.site.register(ComentarioTaller)
