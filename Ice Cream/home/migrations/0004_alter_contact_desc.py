# Generated by Django 5.1.6 on 2025-02-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_rename_message_contact_desc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="desc",
            field=models.TextField(max_length=500),
        ),
    ]
