from django.db import models

# Create your models here.


class HealthCenter(models.Model):
    healthCenter_id = models.BigAutoField(primary_key=True)
    healthCenter_name = models.CharField(max_length=25)
    contactInfo = models.CharField(max_length=11)
    residents = models.ManyToManyField('CreateAccount.Resident', through="Appointment")

    def __str__(self):
        return self.healthCenter_name

    class Meta:
        db_table = "HealthCenter"


class Appointment(models.Model):
    appointment_id = models.BigAutoField(primary_key=True)
    dateOfAppointment = models.DateField()
    timeOfAppointment = models.TimeField()
    dateOfApproval = models.DateField()
    appointmentStatus = models.CharField(max_length=10)
    resident = models.ForeignKey('CreateAccount.Resident', on_delete=models.CASCADE)
    healthCenter = models.ForeignKey(HealthCenter, on_delete=models.CASCADE)

    class Meta:
        db_table = "Appointment"