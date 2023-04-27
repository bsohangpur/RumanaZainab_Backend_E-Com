# Generated by Django 4.2 on 2023-04-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Data", "0005_product_ratings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="ratings",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="products", to="Data.rating"
            ),
        ),
    ]