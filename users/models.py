from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class Doctor(models.Model):

    speciality = models.CharField(
        max_length=2,
        choices=SPECIALITY_CHOICES,
        default=PEDIATRIC,
    )
    photo = models.ImageField()
    description = models.TextField(max_length=512)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}, doctor of {self.speciality}'


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    phone = models.CharField(max_length=13, default='', blank=True)
    certificate_of_insurance = models.CharField(max_length=12, default='', blank=True)

    def __str__(self):
        return f'Patient {self.user.first_name} {self.user.last_name}'


@receiver(post_save, sender=User)
def create_doctor(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)



