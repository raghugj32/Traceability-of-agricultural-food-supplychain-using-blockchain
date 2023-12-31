# Generated by Django 2.0.5 on 2021-08-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy_product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pid', models.CharField(max_length=300)),
                ('pname', models.CharField(max_length=300)),
                ('brand', models.CharField(max_length=300)),
                ('qunatity', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='farmer_payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('farmerid', models.CharField(max_length=300)),
                ('farmername', models.CharField(max_length=300)),
                ('pname', models.CharField(max_length=300)),
                ('total_price', models.CharField(max_length=300)),
                ('card_number', models.CharField(max_length=300)),
                ('cvv', models.CharField(max_length=300)),
                ('cname', models.CharField(max_length=300)),
                ('card_validity', models.CharField(max_length=300)),
                ('phash1', models.CharField(max_length=300)),
                ('newhash1', models.CharField(max_length=300)),
                ('atimestamp', models.CharField(max_length=300)),
            ],
        ),
    ]
