from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def help(request):
    webpage_list = AccessRecord.objects.order_by("date")
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_project/help.html', context=date_dict)
