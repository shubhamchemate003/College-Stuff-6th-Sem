from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

# Register your models here.

admin.site.register(Item)
admin.site.register(Order)




# admin.site.register(UserPost)
# admin.site.register(PostComment)
# admin.site.register(PostLike)