from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def appointment(request):
    return render(request, 'visits/appointment.html')

@login_required(login_url='/login/')
def all(request):
    return render(request, 'all.html')

@login_required(login_url='/login/')
def detail(request, visit_id):
    return render(request, 'visits/details.html')

@login_required(login_url='/login/')
def therapy(request):
    return render(request, 'visits/therapy.html')