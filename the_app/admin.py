from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Reviews)
admin.site.register(Room)
admin.site.register(Cuisine)
admin.site.register(Reservation)
admin.site.register(HotelRelation)

# admin.site.register(Payments)