# Generated by Django 5.1.6 on 2025-02-09 10:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
