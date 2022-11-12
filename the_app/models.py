from django.db import models


class Hotel(models.Model):
    hotel_id = models.CharField(primary_key=True, max_length=5)
    field_hotel_name = models.CharField(db_column='\u2002\u2002\u2002\u2002hotel_name', max_length=50)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    address = models.CharField(max_length=40, null=False)
    city = models.CharField(max_length=30)
    amenities = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'hotel'


class Cuisine(models.Model):
    cuisine_id = models.AutoField(primary_key=True)
    cuisine = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cuisine'


class HotelRelation(models.Model):
    relation_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING)
    cuisine = models.ForeignKey(Cuisine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hotel_relation'
        

class Customer(models.Model):
    cust_id = models.CharField(primary_key=True, max_length=10)
    pword = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'customer'


class Manager(models.Model):
    manager_id = models.CharField(primary_key=True, max_length=10)
    pword = models.CharField(max_length=20)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'manager'


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    room_id= models.IntegerField()
    room_no = models.CharField(max_length=10)
    cust = models.ForeignKey(Customer, models.DO_NOTHING)
    hotel_id = models.CharField(max_length=5)
    reser_time = models.TimeField()
    checkin = models.DateField()
    checkout = models.DateField()

    class Meta:
        managed = False
        db_table = 'reservation'



class Reviews(models.Model):
    review_id = models.CharField(primary_key=True, max_length=10)
    cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, blank=True)
    rating = models.IntegerField(blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING)
    room_no = models.CharField(max_length=10)
    room_type = models.CharField(max_length=15)
    available = models.CharField(max_length=3)
    price = models.CharField(max_length=6)
    air_conditioned = models.BooleanField()
    accomodities = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'
