from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.utils.functional import lazy
from emprendeespiritu.app.talleres.models import Taller, SemanaTaller, ComentarioTaller, LikeTaller
from emprendeespiritu.app.talleres.forms import CommentTallerForm


# Create your views here.


def taller_specific(request, *args, **kwargs):
    taller = Taller.objects.get(pk=kwargs['id'])
    semanas = SemanaTaller.objects.filter(taller=kwargs['id'])
    comentarios = ComentarioTaller.objects.filter(taller=kwargs['id'])
    likes = LikeTaller.objects.filter(taller=kwargs['id']).count()
    if request.user.is_authenticated:
        like_me=LikeTaller.objects.filter(taller=kwargs['id'], author=request.user.id).count()
    else:
        like_me=0
    commentForm = CommentTallerForm()
    context = {
        'is_single': 'True',
        'taller': taller,
        'semanas':semanas,
        'commentForm':commentForm,
        'comentarios':comentarios,
        'likes':likes,
        'like_me':like_me
        }
    return render_to_response('taller/single.html',
                              context,
                              context_instance=RequestContext(request)
                              )
def comentario_taller(request, *args, **kwargs):
    form = CommentTallerForm(request.POST)
    id_taller=kwargs['taller']
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
            return redirect('/taller/single/%s'%(id_taller))
    return redirect('/taller/single/%s'%(id_taller))

def like_taller(request, *args, **kwargs):
    taller=Taller.objects.get(pk=kwargs['taller'])
    likeTaller=LikeTaller(
            taller=taller,
            author=request.user
        )
    if likeTaller:
        likeTaller.save()
        return redirect('/taller/single/%s'%(taller.id))

def dislike_taller(request, *args, **kwargs):
    taller=Taller.objects.get(pk=kwargs['taller'])
    dislikeTaller=LikeTaller.objects.filter(
            taller=taller,
            author=request.user
        )
    if dislikeTaller:
        dislikeTaller.delete()
        return redirect('/taller/single/%s'%(taller.id))