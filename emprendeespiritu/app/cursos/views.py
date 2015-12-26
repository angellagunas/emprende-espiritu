from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.utils.functional import lazy
from emprendeespiritu.app.cursos.models import Curso, SemanaCurso, ComentarioCurso, LikeCurso, SuscripcionCurso
from emprendeespiritu.app.cursos.forms import CommentCourseForm
from emprendeespiritu.app.talleres.models import Taller

# Create your views here.


def get_all(request):
    cursos = Curso.objects.all().order_by('-fecha_creacion')
    talleres = Taller.objects.all().order_by('-fecha_creacion')
    context = {
        "is_blog": "True",
        "cursos": cursos,
        "talleres": talleres,
        "is_dashboard": "True"
    }
    return render_to_response(
        'curso/list.html',
        context,
        context_instance=RequestContext(request)
    )


def course_specific(request, *args, **kwargs):
    curso = Curso.objects.get(pk=kwargs['id'])
    is_request = False

    if request.user.is_authenticated():
        suscripcion = SuscripcionCurso.objects.filter(
            usuario=request.user,
            curso=curso
        ).count()
    else:
        suscripcion = 0

    if suscripcion > 0:
        is_request = True

    if request.user.is_authenticated:
        like_me = LikeCurso.objects.filter(
            curso=kwargs['id'], author=request.user.id).count()
    else:
        like_me = 0

    commentForm = CommentCourseForm()
    context = {
        'is_request': is_request,
        'is_single': 'True',
        'curso': curso,
        'commentForm': commentForm,
        'like_me': like_me
    }
    return render_to_response('curso/single.html',
                              context,
                              context_instance=RequestContext(request)
                              )


@login_required
def comentario_curso(request, *args, **kwargs):
    form = CommentCourseForm(request.POST)
    id_curso = kwargs['curso']
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
            return redirect('/curso/single/%s' % (id_curso))
    return redirect('/curso/single/%s' % (id_curso))


@login_required
def like_curso(request, *args, **kwargs):
    curso = Curso.objects.get(pk=kwargs['curso'])
    likeCurso = LikeCurso(
        curso=curso,
        author=request.user
    )
    if likeCurso:
        likeCurso.save()
        return redirect('/curso/single/%s' % (curso.id))


@login_required
def dislike_curso(request, *args, **kwargs):
    curso = Curso.objects.get(pk=kwargs['curso'])
    dislikeCurso = LikeCurso.objects.filter(
        curso=curso,
        author=request.user
    )
    if dislikeCurso:
        dislikeCurso.delete()
        return redirect('/curso/single/%s' % (curso.id))


@login_required
def request_curso(request, *args, **kwargs):
    curso = Curso.objects.get(pk=kwargs['curso'])
    suscripcion = SuscripcionCurso.objects.get_or_create(
        usuario=request.user,
        curso=curso
    )
    if suscripcion:
        return redirect('/curso/single/%s' % (curso.id))
