# Generated by Django 2.0.5 on 2021-07-29 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_company', '0003_auto_20210729_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance_company_register',
            old_name='fullname',
            new_name='company_name',
        ),
    ]
