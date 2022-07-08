from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # context is the data that will be passed to 'templates/index.html'
    context = {}
    # html template was configured in settings
    return render(request, "templates/index.html", context)
