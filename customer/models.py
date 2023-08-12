from django.db import models

# Create your models here.
class customer_reg(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    mobile = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    password = models.CharField(max_length=300)


class customer_payment1(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=300)
    customer_name = models.CharField(max_length=300)
    retailer_name = models.CharField(max_length=300)
    pname = models.CharField(max_length=300)
    total_price = models.CharField(max_length=300)
    card_number = models.CharField(max_length=300)
    cvv = models.CharField(max_length=300)
    cname = models.CharField(max_length=300)
    card_validity = models.CharField(max_length=300)
    phash1 = models.CharField(max_length=300)
    newhash1 = models.CharField(max_length=300)
    atimestamp = models.CharField(max_length=300)

