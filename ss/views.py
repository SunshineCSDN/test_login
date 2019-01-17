from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ss.models import User
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request, 'ss/index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'ss/login.html')
    else:
        username = request.POST.get('username')
        password =  request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user.username == username and user.password == password:
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('login'))


def reg(request):
    if request.method == 'GET':
        return render(request, 'ss/register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        q = User(username=username, password=password)
        q.save()
        return HttpResponseRedirect(reverse('login'))
