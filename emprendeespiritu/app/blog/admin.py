from django.contrib import admin

from emprendeespiritu.app.blog.models import Entrada, ComentarioBlog, LikeEntrada

admin.site.register(Entrada)
admin.site.register(ComentarioBlog)
admin.site.register(LikeEntrada)