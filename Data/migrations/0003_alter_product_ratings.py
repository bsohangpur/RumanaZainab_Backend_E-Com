# Generated by Django 4.2 on 2023-04-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Data", "0002_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="ratings",
            field=models.ManyToManyField(
                blank=True, related_name="products", to="Data.rating"
            ),
        ),
    ]