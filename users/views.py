from django.contrib.auth.models import User
from .models import Patient, Doctor
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpPatientForm, SignUpDoctorForm
# Create your views here.


def signup_doc(request):
    return render(request, 'users/signup_doc.html')


def signup_patient(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'users/signup_patient.html', {'error': 'Username has been already taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],
                                           password=request.POST['password1'],
                                           first_name=request.POST['first_name'],
                                           last_name=request.POST['last_name'],
                                           email=request.POST['email'])
                patient = user.patient
                patient.phone=request.POST['phone']
                patient.certificate_of_insurance=request.POST['certificate_of_insurance']
                login(request, patient.user)
                return redirect('home')
        else:
            return render(request, 'users/signup_patient.html', {'error':'Passwords must match.'})

    return render(request, 'users/signup_patient.html')
