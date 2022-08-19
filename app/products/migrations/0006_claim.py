# Generated by Django 4.1a1 on 2022-08-19 16:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0005_product_users_saves"),
    ]

    operations = [
        migrations.CreateModel(
            name="Claim",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("date", models.DateField(auto_now_add=True)),
                ("name", models.CharField(max_length=200)),
                ("code", models.BigIntegerField()),
                ("brand", models.CharField(max_length=200)),
                ("user_comment", models.TextField(max_length=600)),
                ("admin_comment", models.TextField(max_length=600)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepté", "Accepté"),
                            ("Traitement en cours", "Traitement en cours"),
                            ("Refusé", "Refusé"),
                        ],
                        default="Traitement en cours",
                        max_length=20,
                    ),
                ),
                ("deal", models.BooleanField(default=False)),
                ("user", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]