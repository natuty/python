from django.http import HttpResponse
import django
def hello(request):
	return HttpResponse("Hello World")
print django.get_version()