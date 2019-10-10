from django.db import models
from users import models as acc_models

# Create your models here.
class Visit(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(acc_models.Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(acc_models.Patient, on_delete=models.CASCADE)
    problem = models.TextField(max_length=128)
    therapy = models.TextField(max_length=512)

