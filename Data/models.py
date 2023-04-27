from django.db import models

# Create your models here.


class Rating(models.Model):
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.rate} ({self.count})'


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/product')
    ratings = models.ManyToManyField('Rating', related_name='products', blank=True, null=True)

    def __str__(self):
        return self.title