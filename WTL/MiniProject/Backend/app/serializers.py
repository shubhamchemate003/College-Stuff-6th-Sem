from rest_framework import serializers
from rest_framework import permissions
from .models import *

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

	class Meta:
		model = Order
		fields = ['item','quantity','cost','delivery_time']
