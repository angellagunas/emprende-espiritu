from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.utils.functional import lazy
from emprendeespiritu.app.cursos.models import Curso, SemanaCurso, ComentarioCurso, LikeCurso
from emprendeespiritu.app.cursos.forms import CommentCourseForm

# Create your views here.

def course_specific(request, *args, **kwargs):
    curso = Curso.objects.get(pk=kwargs['id'])
    semanas = SemanaCurso.objects.filter(curso=kwargs['id'])
    comentarios = ComentarioCurso.objects.filter(curso=kwargs['id'])
    likes = LikeCurso.objects.filter(curso=kwargs['id']).count()
    if request.user.is_authenticated:
        like_me=LikeCurso.objects.filter(curso=kwargs['id'], author=request.user.id).count()
    else:
        like_me=0
    commentForm = CommentCourseForm()
    context = {
        'is_single': 'True',
        'curso': curso,
        'semanas':semanas,
        'commentForm':commentForm,
        'comentarios':comentarios,
        'likes':likes,
        'like_me':like_me
        }
    return render_to_response('curso/single.html',
                              context,
                              context_instance=RequestContext(request)
                              )

def comentario_curso(request, *args, **kwargs):
    form = CommentCourseForm(request.POST)
    id_curso=kwargs['curso']
    if request.method == 'POST':
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            curso = Curso.objects.get(pk=id_curso)
            comentario = ComentarioCurso(
                comentario=comentario,
                author=request.user,
                curso=curso
                )
            comentario.save()
            return redirect('/curso/single/%s'%(id_curso))
    return redirect('/curso/single/%s'%(id_curso))

def like_curso(request, *args, **kwargs):
    curso=Curso.objects.get(pk=kwargs['curso'])
    likeCurso=LikeCurso(
            curso=curso,
            author=request.user
        )
    if likeCurso:
        likeCurso.save()
        return redirect('/curso/single/%s'%(curso.id))

def dislike_curso(request, *args, **kwargs):
    curso=Curso.objects.get(pk=kwargs['curso'])
    dislikeCurso=LikeCurso.objects.filter(
            curso=curso,
            author=request.user
        )
    if dislikeCurso:
        dislikeCurso.delete()
        return redirect('/curso/single/%s'%(curso.id))