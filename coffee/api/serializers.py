from rest_framework import serializers
from . import models


class CoffeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'location', 'images', 'created_at', 'updated_at',)
        model = models.Coffee
