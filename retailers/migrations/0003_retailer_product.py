# Generated by Django 2.0.5 on 2021-08-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0002_retailer_payment1'),
    ]

    operations = [
        migrations.CreateModel(
            name='retailer_product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('retailer_id', models.CharField(max_length=300)),
                ('retailer_name', models.CharField(max_length=300)),
                ('product_name', models.CharField(max_length=300)),
                ('quantity', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('product_image', models.FileField(upload_to='')),
            ],
        ),
    ]
