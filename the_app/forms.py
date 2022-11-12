from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Hotel, Customer, Cuisine, Manager, Reviews, Room


class MyCustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_no', 'cust_id', 'pword']


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        exclude = ['host', 'participants']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'