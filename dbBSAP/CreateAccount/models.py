from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    type = (("R", "Resident"), ("O", "Organization"), ("A", "Admin"))
    user_type = models.CharField(max_length=1, choices=type)

    class Meta:
        abstract = True


class Resident(User):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    birth_date = models.DateField()
    present_address = models.CharField(max_length=50)
    borrowed_resources = models.ManyToManyField("BorrowResource.Resource", through="BorrowResource.BorrowResource")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "Resident"


class Organization(User):
    organization_name = models.CharField(max_length=50)
    borrowed_resources = models.ManyToManyField("BorrowResource.Resource", through="BorrowResource.BorrowResource")

    def __str__(self):
        return self.organization_name

    class Meta:
        db_table = "Organization"


class Admin(User):
    admin_status = models.CharField(max_length=1, choices=(("A", "Active"), ("I", "Inactive")))
    approve_event = models.OneToOneField("OrganizeEvent.Event", on_delete=models.CASCADE)
    approve_appointment = models.OneToOneField("BookAppointment.Appointment", on_delete=models.CASCADE)
    approve_borrowing = models.OneToOneField("BorrowResource.BorrowResource", on_delete=models.CASCADE)

    def __str__(self):
        return "admin"

    class Meta:
        db_table = "Admin"


class CreateAccount:
    pass