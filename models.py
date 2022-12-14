# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cuisine(models.Model):
    cuisine_id = models.CharField(primary_key=True, max_length=10)
    cuisine = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cuisine'


class Customer(models.Model):
    cust_id = models.CharField(primary_key=True, max_length=10)
    pword = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hotel(models.Model):
    hotel_id = models.CharField(primary_key=True, max_length=5)
    field_hotel_name = models.CharField(db_column='\u2002\u2002\u2002\u2002hotel_name', max_length=50)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=30, blank=True, null=True)
    amenities = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel'


class HotelRelation(models.Model):
    hotel = models.OneToOneField(Hotel, models.DO_NOTHING, primary_key=True)
    cuisine = models.ForeignKey(Cuisine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hotel_relation'
        unique_together = (('hotel', 'cuisine'),)


class Manager(models.Model):
    manager_id = models.CharField(primary_key=True, max_length=10)
    pword = models.CharField(max_length=20)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'manager'


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    room_no = models.CharField(max_length=10, blank=True, null=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    hotel_id = models.CharField(max_length=5, blank=True, null=True)
    reser_time = models.TimeField()
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reservation'


class Reviews(models.Model):
    review_id = models.CharField(primary_key=True, max_length=10)
    cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, blank=True, null=True)
    room_no = models.CharField(max_length=10)
    room_type = models.CharField(max_length=15)
    available = models.CharField(max_length=3)
    price = models.CharField(max_length=6)
    air_conditioned = models.IntegerField()
    accomodities = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'
