from django.db import models
# Create your models here.


class Resource(models.Model):
    resource_id = models.BigAutoField(primary_key=True)
    resource_quantity = models.IntegerField()
    resource_name = models.CharField(max_length=25)
    is_available = models.BooleanField()

    def __str__(self):
        return self.resource_name

    class Meta:
        db_table = "Resource"


class BorrowResource(models.Model):
    borrow_resources_id = models.BigAutoField(primary_key=True)
    resident_id = models.ForeignKey("CreateAccount.Resident", on_delete=models.CASCADE)
    org_id = models.ForeignKey("CreateAccount.Organization", on_delete=models.CASCADE)
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    borrow_date = models.DateField()
    return_date = models.DateField()

    class Meta:
        db_table = "BorrowResource"
