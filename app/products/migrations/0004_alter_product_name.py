# Generated by Django 3.2rc1 on 2021-05-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_auto_20210324_0210"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
