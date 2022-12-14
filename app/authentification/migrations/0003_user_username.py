# Generated by Django 3.2.3 on 2021-06-17 00:06

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentification", "0002_remove_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(
                default="user",
                error_messages={
                    "unique": "A user with that username already exists."
                },
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[
                    django.contrib.auth.validators.UnicodeUsernameValidator()
                ],
                verbose_name="username",
            ),
            preserve_default=False,
        ),
    ]
