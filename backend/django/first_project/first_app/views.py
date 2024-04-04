from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def help(request):
    my_dict = {'insert_here': 'I am the help view function'}
    return render(request, 'first_project\help.html', context=my_dict)
