# Generated by Django 3.2.3 on 2021-06-13 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentification", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
