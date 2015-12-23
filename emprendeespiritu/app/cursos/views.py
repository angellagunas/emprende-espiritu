from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template 

# Create your views here.

def course_specific(request):
    template = get_template("curso/single.html")
    cursos = Curso.objects.all()
    context = Context({ "is_blog": "True", "cursos":cursos, "request":request })
    return HttpResponse(template.render(context))