from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from emprendeespiritu.app.home.forms import LoginForm
from emprendeespiritu.app.cursos.models import Curso, SuscripcionCurso
from emprendeespiritu.app.talleres.models import Taller
from emprendeespiritu.app.email.tasks import send_mail
from emprendeespiritu.app.perfil.forms import UserForm

# Create your views here.


def index_view(request):
    return redirect('vista_index')


def login_view(request):
    msg = ""
    form = LoginForm(request.POST)
    formSign = UserForm()
    cursos = Curso.objects.all()
    talleres = Taller.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('vista_dashboard')
            else:
                msg = "Usuario y/o password incorrecto"
    else:
        form = LoginForm()

    return render_to_response('index.html',
                              {
                                  'form': form,
                                  'formSign': formSign,
                                  'msg': msg,
                                  'cursos': cursos,
                                  'talleres': talleres,
                              },
                              context_instance=RequestContext(request)
                              )

@login_required
def dashboard_view(request):
    template = get_template("home/dashboard.html")

    mis_cursos = SuscripcionCurso.objects.filter(usuario=request.user.id
    ).values_list('curso', flat=True)

    cursos = Curso.objects.filter(
        id__in = mis_cursos
    ).order_by(
        '-fecha_creacion'
    )
    
    talleres = Taller.objects.filter().order_by('-fecha_creacion')

    context = {
        "is_blog": "True",
        "cursos": cursos,
        "talleres": talleres,
        "is_dashboard": "True"
    }
    return render_to_response(
        'home/dashboard.html',
        context,
        context_instance=RequestContext(request)
    )


def send_mail_view(request):
    if request.method == 'POST':
        fname = request.POST.get('contactName')
        email = request.POST.get('contactEmail')
        msg = request.POST.get('contactMessage')
        send_mail(fname, email, msg)
    return redirect('vista_index')

@login_required
def logout_view(request):
    logout(request)
    return redirect('vista_index')
