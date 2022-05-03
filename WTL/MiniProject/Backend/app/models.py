from django.db import models
from django.db.models.fields import related
from usermanager.models import *
from django.utils import timezone
import os
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Item(models.Model):
    def upload_to(instance, filename):
        now = timezone.now()
        base, extension = os.path.splitext(filename.lower())
        milliseconds = now.microsecond // 1000
        return f"item/{instance.id}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

    name=models.TextField(max_length=200000,null = True, blank = True, default = 'Unknown')
    owner = models.ForeignKey(Account, related_name='item_owner', on_delete=models.CASCADE, null=True , blank= True)
    price=models.IntegerField(null=True,blank=True,default=100)
    original_price=models.IntegerField(null=True,blank=True,default=100)
    image=models.ImageField(_("Image"), upload_to=upload_to, blank=True, null=True, default="default.jpg")
    # tag=models.ManyToManyField(Tag,null = True, blank = True,related_name='itemtag')
    
    def __str__(self):
        return str(self.name)

class Order(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,related_name='order_item',null=False, blank=False)
    delivery_time = models.DateTimeField(null = True, blank = True)
    is_active=models.BooleanField(null = True, default = True)
    quantity=models.IntegerField(null=True,blank=True,default=1)
    customer=models.ForeignKey(Account, related_name='customer', on_delete=models.CASCADE, null=True , blank= True)
    delivery_personnel=models.ForeignKey(Account, related_name='order_dp', on_delete=models.CASCADE, null=True , blank= True)
    cost=models.IntegerField(null=True,blank=True,default=100)

    def __str__(self):
        return str(self.item)
