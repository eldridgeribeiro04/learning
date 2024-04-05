from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users

# Create your views here.
def index(request):
    user_data = Users.objects.order_by('first_name')
    user_dict = {'user_records': user_data}
    return render(request, 'MyApp/index.html', context=user_dict)
