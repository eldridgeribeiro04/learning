from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'templates_app/index.html')


def base(request):
    return render(request, 'templates_app/base.html')


def other(request):
    return render(request, 'templates_app/other.html')


def relative_url(request):
    return render(request, 'templates_app/relative_url_templates.html')