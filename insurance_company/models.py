from django.db import models

# Create your models here.
class insurance_company_register(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=300)
    mobile = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    password = models.CharField(max_length=300)