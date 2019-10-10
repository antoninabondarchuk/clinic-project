from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Patient, Doctor
from django.contrib.auth.models import User

CARDIOLOGY = "CD"
DERMATOLOGY = "DM"
GASTROENTEROLOGY = "GE"
GYNECOLOGY = "GC"
NEUROLOGY = "NL"
PEDIATRIC = "PD"
UROLOGY = "UR"

SPECIALITY_CHOICES = [
        (CARDIOLOGY, 'Cardiology'),
        (DERMATOLOGY, 'Dermatology'),
        (GASTROENTEROLOGY, 'Gastroenterology'),
        (GYNECOLOGY, 'Gynecology'),
        (NEUROLOGY, 'Neurology'),
        (PEDIATRIC, 'Pediatric'),
        (UROLOGY, 'Urology'),
    ]

class SignUpPatientForm(UserCreationForm):
    phone = forms.CharField(max_length=13, label="Phone")
    certificate_of_insurance = forms.CharField(max_length=12,
                                               label='Certificate of insurance')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username',
                  'password1', 'password2', 'certificate_of_insurance',)



class SignUpDoctorForm(UserCreationForm):
    photo = forms.ImageField(label="Photo")
    description = forms.CharField(max_length=512, widget=forms.Textarea,
                                  label='Description', help_text='Enter your education and certificates')

    speciality = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=SPECIALITY_CHOICES,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'photo', 'description', 'speciality',)
