from rest_framework import serializers
from .models import *


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'

    def validate(self, data):
        mrp = data.get('mrp')
        pricing = data.get('pricing')

        if pricing is not None and mrp is not None and pricing > mrp:
            raise serializers.ValidationError("Pricing should not be greater than MRP")

        return data


class ShippingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipping
        fields = '__all__'
