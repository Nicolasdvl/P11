# Generated by Django 3.2.7 on 2021-09-18 13:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0004_alter_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="users_saves",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
