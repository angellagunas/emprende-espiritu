from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template 
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from emprendeespiritu.app.home.forms import LoginForm
from emprendeespiritu.app.cursos.models import Curso
from emprendeespiritu.app.talleres.models import Taller
from emprendeespiritu.app.email.tasks import send_mail

# Create your views here.
def index_view(request):
    return redirect('vista_index')

def login_view(request):
    msg = ""
    form = LoginForm(request.POST)

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
                              {'form': form, 'msg': msg},
                              context_instance=RequestContext(request)
                              )

def dashboard_view(request):
    template = get_template("home/dashboard.html")
    cursos = Curso.objects.all()
    talleres = Taller.objects.all()
    context = {
        "is_blog":"True",
        "cursos": cursos,
        "talleres": talleres,
        "is_dashboard" : "True"
    }
    return render_to_response(
        'home/dashboard.html',
        context,
        context_instance=RequestContext(request)
        )

def send_mail_view(request):
    if request.method == 'POST':
        fname=request.POST.get('contactName')
        email=request.POST.get('contactEmail')
        msg=request.POST.get('contactMessage')
        send_mail(fname, email, msg)
    return redirect('vista_index')

def logout_view(request):
    logout(request)
    return redirect('vista_index')