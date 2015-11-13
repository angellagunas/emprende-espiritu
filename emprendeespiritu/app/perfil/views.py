from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template 

# Create your views here.
def index_view(request):
	template = get_template("index.html")
	context = Context({})
	return HttpResponse(template.render(context))