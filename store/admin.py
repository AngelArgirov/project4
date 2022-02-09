from django.contrib import admin
from .models import *

# Register your models here.

from .models import Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
