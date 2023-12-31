# Generated by Django 2.0.5 on 2021-08-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_buy_product_farmer_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='insurance_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farmerid', models.CharField(max_length=300)),
                ('farmername', models.CharField(max_length=300)),
                ('farmer_fullname', models.CharField(max_length=300)),
                ('door_number', models.CharField(max_length=300)),
                ('locality', models.CharField(max_length=300)),
                ('village', models.CharField(max_length=300)),
                ('district', models.CharField(max_length=300)),
                ('pincode', models.CharField(max_length=300)),
                ('community', models.CharField(max_length=300)),
                ('farmer_category', models.CharField(max_length=300)),
                ('account_number', models.CharField(max_length=300)),
                ('bank_branch', models.CharField(max_length=300)),
                ('mobile', models.CharField(max_length=300)),
                ('survey_number', models.CharField(max_length=300)),
                ('seed_name', models.CharField(max_length=300)),
            ],
        ),
    ]
