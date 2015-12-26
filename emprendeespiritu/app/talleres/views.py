from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.utils.functional import lazy
from emprendeespiritu.app.talleres.models import Taller, SemanaTaller, ComentarioTaller, LikeTaller, SuscripcionTaller
from emprendeespiritu.app.talleres.forms import CommentTallerForm


# Create your views here.


def taller_specific(request, *args, **kwargs):
    taller = Taller.objects.get(pk=kwargs['id'])
    is_request = False

    if request.user.is_authenticated():
        suscripcion = SuscripcionTaller.objects.filter(
            usuario=request.user,
            taller=taller
        ).count()
    else:
        suscripcion = 0

    if suscripcion > 0:
        is_request = True

    if request.user.is_authenticated:
        like_me = LikeTaller.objects.filter(
            taller=kwargs['id'], author=request.user.id).count()
    else:
        like_me = 0

    commentForm = CommentTallerForm()
    context = {
        'is_request': is_request,
        'is_single': 'True',
        'taller': taller,
        'commentForm': commentForm,
        'like_me': like_me
    }
    return render_to_response('taller/single.html',
                              context,
                              context_instance=RequestContext(request)
                              )


@login_required
def comentario_taller(request, *args, **kwargs):
    form = CommentTallerForm(request.POST)
    id_taller = kwargs['taller']
    if request.method == 'POST':
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            taller = Taller.objects.get(pk=id_taller)
            comentario = ComentarioTaller(
                comentario=comentario,
                author=request.user,
                taller=taller
            )
            comentario.save()
            return redirect('/taller/single/%s' % (id_taller))
    return redirect('/taller/single/%s' % (id_taller))


@login_required
def like_taller(request, *args, **kwargs):
    taller = Taller.objects.get(pk=kwargs['taller'])
    likeTaller = LikeTaller(
        taller=taller,
        author=request.user
    )
    if likeTaller:
        likeTaller.save()
        return redirect('/taller/single/%s' % (taller.id))


@login_required
def dislike_taller(request, *args, **kwargs):
    taller = Taller.objects.get(pk=kwargs['taller'])
    dislikeTaller = LikeTaller.objects.filter(
        taller=taller,
        author=request.user
    )
    if dislikeTaller:
        dislikeTaller.delete()
        return redirect('/taller/single/%s' % (taller.id))

@login_required
def request_taller(request, *args, **kwargs):
    taller = Taller.objects.get(pk=kwargs['taller'])
    suscripcion = SuscripcionTaller.objects.get_or_create(
        usuario=request.user,
        taller=taller
    )
    if suscripcion:
        return redirect('/taller/single/%s' % (taller.id))
