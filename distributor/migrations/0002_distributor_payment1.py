# Generated by Django 2.0.5 on 2021-08-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='distributor_payment1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('distributor_id', models.CharField(max_length=300)),
                ('distributor_name', models.CharField(max_length=300)),
                ('farmer_name', models.CharField(max_length=300)),
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