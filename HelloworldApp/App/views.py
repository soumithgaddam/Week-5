from django.http import HttpResponse
import json

def home(request):
	text = { 'Message':'Hello World!'}
	return HttpResponse(json.dumps(text))

# Create your views here.