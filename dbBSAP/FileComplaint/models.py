from django.db import models

# Create your models here.


class Complaint(models.Model):
    complaint_id = models.BigAutoField(primary_key=True)
    complainant = models.ForeignKey("CreateAccount.Resident", on_delete=models.CASCADE)
    details = models.ForeignKey('ComplaintDetails', on_delete=models.CASCADE)
    admin = models.ForeignKey('CreateAccount.Admin', on_delete=models.CASCADE)
    complaint_status = models.CharField(max_length=1, choices=(("R", "Resolved"), ("P", "Pending"), ("E", "Escalation")))
    date_of_complaint = models.DateField(auto_now=True)

    class Meta:
        db_table = "Complaint"


class ComplaintDetails(models.Model):
    complaint_details_id = models.BigAutoField(primary_key=True)
    complaint_type = models.CharField(max_length=1, choices=(("E", "Environment"), ("R", "Resident"), ("B", "Barangay")))
    description = models.TextField()
