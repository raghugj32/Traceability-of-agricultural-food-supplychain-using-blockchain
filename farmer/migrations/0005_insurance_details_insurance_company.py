# Generated by Django 2.0.5 on 2021-08-04 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0004_farmer_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance_details',
            name='insurance_company',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
