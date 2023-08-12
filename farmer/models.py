from django.db import models

# Create your models here.
class farmer_reg(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    mobile = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

class buy_product(models.Model):
    id=models.AutoField(primary_key=True)
    pid=models.CharField(max_length=300)
    pname = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    qunatity= models.CharField(max_length=300)
    price= models.CharField(max_length=300)

class farmer_payment(models.Model):
    id = models.AutoField(primary_key=True)
    farmerid = models.CharField(max_length=300)
    farmername = models.CharField(max_length=300)
    pname = models.CharField(max_length=300)
    total_price = models.CharField(max_length=300)
    card_number = models.CharField(max_length=300)
    cvv = models.CharField(max_length=300)
    cname = models.CharField(max_length=300)
    card_validity = models.CharField(max_length=300)
    phash1 = models.CharField(max_length=300)
    newhash1 = models.CharField(max_length=300)
    atimestamp = models.CharField(max_length=300)

class insurance_details(models.Model):
    id = models.AutoField(primary_key=True)
    farmerid = models.CharField(max_length=300)
    farmername = models.CharField(max_length=300)
    insurance_company = models.CharField(max_length=300)
    farmer_fullname=models.CharField(max_length=300)
    door_number=models.CharField(max_length=300)
    locality=models.CharField(max_length=300)
    village=models.CharField(max_length=300)
    district=models.CharField(max_length=300)
    pincode=models.CharField(max_length=300)
    community=models.CharField(max_length=300)
    farmer_category=models.CharField(max_length=300)
    account_number=models.CharField(max_length=300)
    bank_branch=models.CharField(max_length=300)
    mobile=models.CharField(max_length=300)
    survey_number=models.CharField(max_length=300)
    seed_name=models.CharField(max_length=300)
    status = models.CharField(max_length=300)

class farmer_product(models.Model):
    id = models.AutoField(primary_key=True)
    farmerid = models.CharField(max_length=300)
    farmername = models.CharField(max_length=300)
    product_name=models.CharField(max_length=300)
    quantity = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    product_image = models.FileField()



