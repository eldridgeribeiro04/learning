from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppTwo.models import Users
from .forms import UserForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success/')
    else:
        form = UserForm()
    return render(request, 'MyApp/index.html', {'form': form})


def success(request):
    return render(request, 'MyApp/success.html')