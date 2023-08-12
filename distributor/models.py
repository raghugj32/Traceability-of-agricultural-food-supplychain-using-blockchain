from django.db import models

# Create your models here.
class distributor_reg(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    mobile = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    password = models.CharField(max_length=300)


class distributor_payment1(models.Model):
    id = models.AutoField(primary_key=True)
    distributor_id = models.CharField(max_length=300)
    distributor_name = models.CharField(max_length=300)
    farmer_name = models.CharField(max_length=300)
    pname = models.CharField(max_length=300)
    total_price = models.CharField(max_length=300)
    card_number = models.CharField(max_length=300)
    cvv = models.CharField(max_length=300)
    cname = models.CharField(max_length=300)
    card_validity = models.CharField(max_length=300)
    phash1 = models.CharField(max_length=300)
    newhash1 = models.CharField(max_length=300)
    atimestamp = models.CharField(max_length=300)

class distributor_product(models.Model):
    id = models.AutoField(primary_key=True)
    distributor_id = models.CharField(max_length=300)
    distributor_name = models.CharField(max_length=300)
    product_name=models.CharField(max_length=300)
    quantity = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    product_image = models.FileField()