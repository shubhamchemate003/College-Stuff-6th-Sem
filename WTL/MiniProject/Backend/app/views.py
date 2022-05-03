from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
# Create your views here.
from django.contrib.auth import get_user_model

import datetime
from django.utils.timezone import utc
from django.utils import timezone


User = get_user_model()

def get_delivery_personnel(id):
    dp=list(User.objects.filter(category="delivery_personnel"))
    x=id%len(dp)
    return dp[x]

class AddItems(APIView):
    def post(self,request):
        request_data=request.data
        item=Item.objects.create(name=request_data['name'],price=request_data['price'],original_price=request_data['oprice'],owner=User.objects.get(first_name=request_data['seller']))
        serializer_data=ItemSerializer(item).data
        return Response(serializer_data)

class GetItems(APIView):
    def get(self,request):
        objs=Item.objects.all()
        serializer_data=serialize('json',objs)
        return Response(serializer_data)

class PlaceOrder(APIView):
    permission_classes = ()

    """
    Retrieve, update or delete a snippet instance.
    """
    def post(self, request):
        print(request)
        request_data = request.data
        print(request_data)
        item=Item.objects.filter(id=request_data['item']).first()
        user1 = request.user
        delivery_time = datetime.datetime.utcnow().replace(tzinfo=utc) + datetime.timedelta(days=1)
        cost=(item.price) * request_data['quantity']

        NewOrder = Order.objects.create(item = item,quantity=request_data['quantity'],customer=user1,delivery_time=delivery_time,cost=cost)
        NewOrder.save()
        dp=get_delivery_personnel(NewOrder.id)
        NewOrder.delivery_personnel=dp

        NewOrder.save()

        # self.check_object_permissions(request,user1) # object permission explicitly called

        serializer_data = OrderSerializer(NewOrder).data
        return Response(serializer_data)


class GetCustomerOrders(APIView):

    def get(self,request):
        user1=request.user
        now = timezone.now()
        list1=[]
        orders=Order.objects.filter(delivery_time__gte=now, customer=user1)
        for order in orders:
            serializer_data = OrderSerializer(order).data
            serializer_data['item_name']=order.item.name
            list1.append(serializer_data)

        return Response(list1)

class GetDPOrders(APIView):

    def get(self,request):
        user1=request.user
        list1=[]
        now = timezone.now()
        orders=Order.objects.filter(delivery_time__gte=now, delivery_personnel=user1)
        for order in orders:
            serializer_data = OrderSerializer(order).data
            serializer_data['item_name']=order.item.name
            serializer_data['address']=order.customer.address
            serializer_data['first_name']=order.customer.first_name
            list1.append(serializer_data)

        return Response(list1)