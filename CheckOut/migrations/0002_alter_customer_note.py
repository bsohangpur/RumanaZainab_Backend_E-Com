# Generated by Django 4.2 on 2023-04-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CheckOut", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
    ]
