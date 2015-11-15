from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template 

# Create your views here.
def blog_view(request):
	template = get_template("blog/blog.html")
	context = Context({"is_blog":"True"})
	return HttpResponse(template.render(context))

def blog_specific(request):
	template = get_template("blog/single.html")
	context = Context({ "is_blog": "True" })
	return HttpResponse(template.render(context))