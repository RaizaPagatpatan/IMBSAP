
from django.db import models

# Create your models here.


class Event(models.Model):
    eventID = models.BigAutoField(primary_key=True)
    eventName = models.CharField(max_length=150)
    organizer = models.ForeignKey('CreateAccount.Organization', on_delete=models.CASCADE)
    details = models.CharField(max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()
    event_status = models.CharField(max_length=1, choices=(("P", "Pending"), ("A", "Approved"), ("C", "Cancelled")))
    location = models.TextField()

    def __str__(self):
        return f"{self.eventName} {self.event_status}"
    class Meta:
        db_table = "Event"
