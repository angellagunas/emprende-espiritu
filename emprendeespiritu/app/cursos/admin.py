from django.contrib import admin

from emprendeespiritu.app.cursos.models import Curso, SemanaCurso, ArchivoSemana, ComentarioCurso, LikeCurso, SuscripcionCurso

admin.site.register(Curso)
admin.site.register(SemanaCurso)
admin.site.register(ArchivoSemana)
admin.site.register(ComentarioCurso)
admin.site.register(LikeCurso)
admin.site.register(SuscripcionCurso)
