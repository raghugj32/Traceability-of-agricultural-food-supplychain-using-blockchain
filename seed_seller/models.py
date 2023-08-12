from django.db import models

# Create your models here.
class seedseller_reg(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    mobile = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

class seed_upload(models.Model):
    id = models.AutoField(primary_key=True)
    seed_name=models.CharField(max_length=300)
    number_pieces = models.CharField(max_length=300)
    brand_name = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    product_image = models.FileField()