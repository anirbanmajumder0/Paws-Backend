# Generated by Django 4.2.9 on 2024-02-29 07:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aniresfr', '0004_customuser_no_reports_ngouser_no_received_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngouser',
            name='created_campaigns_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
    ]