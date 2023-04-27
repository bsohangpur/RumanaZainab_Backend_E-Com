from rest_framework import serializers
from .models import Product, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    # ratings = RatingSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description',
                  'category', 'image')
