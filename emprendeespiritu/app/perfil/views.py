from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from emprendeespiritu.app.perfil.forms import UserForm
from emprendeespiritu.app.email.tasks import send_mail

def perfil_view(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            newUser = User(
                username=userForm.cleaned_data['username'],
                password=make_password(userForm.cleaned_data['password'], 'pbkdf2_sha256'),
                first_name=userForm.cleaned_data['first_name'],
                last_name=userForm.cleaned_data['last_name'],
                email=userForm.cleaned_data['email']
            )
            newUser.save()
            if newUser:
                user = authenticate(username=newUser.username, password=newUser.password)
                if user is not None:
                    login(request, user)
                    return redirect('vista_dashboard')
                else:
                    msg = "Usuario y/o password incorrecto"
                    return redirect('vista_index')
            else:
                msg = "Oops, no se pudo guardar tu registro, intentalo mas tarde."
                return redirect('vista_index')
        else:
            msg = "Formulario no valido"
            return redirect('vista_index')
    else:
        return redirect('vista_index')
