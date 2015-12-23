from django.contrib import admin

from emprendeespiritu.app.cursos.models import Curso,SemanaCurso,ArchivoSemana

admin.site.register(Curso)
admin.site.register(SemanaCurso)
admin.site.register(ArchivoSemana)