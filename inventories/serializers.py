from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id_product', 'name', 'description', 'price', 'creation_date', 'update_date',)
        model = models.Product

