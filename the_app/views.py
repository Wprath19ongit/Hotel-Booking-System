from urllib import request, response
from django.http import HttpResponse
from datetime import *
from time import gmtime, strftime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

from .models import Hotel, Cuisine, Customer, Manager, Reviews, Room, Reservation, HotelRelation
# from .forms import RoomForm, UserForm, MyUserCreationForm


def home_page(request):
    return render(request, 'base/home.html',{})



def login_page(request):
    if(request.method=="POST"):
        
        m_username = request.POST.get('M_name')
        m_pword = request.POST.get('M_pword') 
        c_username = request.POST.get('C_name')
        c_pword = request.POST.get('C_pword')
        msg = "Username OR password does not exit"
        context1 = {'msg1': msg}
        if(m_username != None and m_pword != None):
            try:
                user = Manager.objects.get(manager_id = m_username)    
               
                if user.pword == m_pword:
                    return redirect('manager_page', pk=user.manager_id)
                else:
                    return render(request,'base/login.html',context1)
            except:
                return render(request,'base/login.html',context1)
        # else:
            
        context2 = {'msg2': msg}
                
        if(c_username!="" and c_pword!=""):
            try:
                user = Customer.objects.get(cust_id = c_username)
                thecontext = {'user':user}
                if user.pword==c_pword:
                    return redirect('hotel',pk=user.cust_id)
                else:
                    return render(request,'base/login.html',context2)
            except:
                return render(request,'base/login.html',context2)

    return render(request, 'base/login.html',{})

def logout_page(request):
    return redirect('home_page')

def register_page(request):
    if(request.method=="POST"):

        username = request.POST.get('uname')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pword = request.POST.get('pword')
        phone_no = request.POST.get('phone')
        
        if(username != None and fname != None and lname != None and email != None and pword != None and phone_no != None):
            try:
                msg1 = "Username already exists"
                cus = Customer.objects.get(cust_id = username)
                if(cus!=None):
                    return render(request,'base/register.html',{'msg1':msg1})
            except:
                Customer.objects.create(cust_id=username, pword=pword, first_name=fname, last_name=lname, email=email, phone_no=phone_no)
                return redirect(login_page)
            else:
                msg1 = "Details filled incorrectly"
                return render(request,'base/register.html',{'msg1':msg1})
    msg1=""           
    return render(request,'base/register.html',{'msg1':msg1})
        


def manager_page(request, pk):
    man = Manager.objects.get(manager_id=pk)
    hot = Hotel.objects.get(hotel_id=man.hotel.hotel_id)
    q1 = request.GET.get('q1') if request.GET.get('q1') != None else ''

    room = Room.objects.filter(
        Q(hotel=hot.hotel_id) &
        (Q(room_type__icontains=q1) |
        Q(available__icontains=q1) |
        Q(price__icontains=q1) |
        Q(accomodities__icontains=q1) |
        Q(air_conditioned__icontains=q1)
    ))
    q2 = request.GET.get('q2') if request.GET.get('q2') != None else ''

    review = Reviews.objects.filter(
        Q(hotel=hot.hotel_id) &
        (Q(rating__icontains=q2) |
        Q(comments__icontains=q2))
    )
    context = {'man': man, 'hotel':hot, 'room':room,'review':review}


    return render(request,'base/manager.html',context)

def check_room(room_id):
    res = Reservation.objects.get(room_id=room_id)
    abhi = str(datetime.now().date)
    # if(abhi)

def hotel(request, pk):
    cus = Customer.objects.get(cust_id=pk)
    rooms = Room.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    res = Reservation.objects.all()
    hotels = Hotel.objects.filter(
        Q(field_hotel_name__icontains=q) |
        Q(amenities__icontains=q) |
        Q(city__icontains=q) |
        Q(address__icontains=q)
    )
    hotel_rel = HotelRelation.objects.all()
    cuisine = Cuisine.objects.all()
    hotels_count = hotels.count()
    now = (datetime.now().date)
    context = {'hotels': hotels, 'h_count': hotels_count, 'cus':cus, 'rooms':rooms,'res':res,'now':now,'cuisine':cuisine,'food':hotel_rel }
    return render (request, 'base/hotels.html',context)


def update_cust_page(request,pk):
    cus = Customer.objects.get(cust_id=pk)
    msg1=""
    context={'cus':cus,'msg1':msg1}
    if(request.method=="POST"):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pword = request.POST.get('pword')
        phone_no = request.POST.get('phone')
        
        if(fname != None and lname !=None  and email != None and pword != None and phone_no != None):
            Customer.objects.filter(cust_id=cus.cust_id).update(pword=pword, first_name=fname, last_name=lname, email=email, phone_no=phone_no)
            return redirect('hotel',pk=cus.cust_id)
        else:
            msg1 = "Details filled incorrectly"
            return render(request,'base/update_cust.html',context)
        
    return render(request,'base/update_cust.html',context)


def update_hotel_page(request,pk):
    hot = Hotel.objects.get(hotel_id=pk)
    msg1=""
    man = Manager.objects.get(hotel=hot.hotel_id)
    context={'hot':hot,'msg1':msg1}
    if(request.method=="POST"):
        hname = request.POST.get('hname')
        address = request.POST.get('address')
        city = request.POST.get('city')
        amenities = request.POST.get('amenities')
        if(hname != None and address != None and city != None and amenities != None):
            Hotel.objects.filter(hotel_id=hot.hotel_id).update(field_hotel_name=hname, address=address,city=city, amenities=amenities)
            return redirect('manager_page',pk=man.manager_id)
        else:
            msg1 = "Details filled incorrectly"
            return render(request,'base/update_hotel.html',context)
      
    return render(request,'base/update_hotel.html',context)



def update_man_page(request,pk):
    man = Manager.objects.get(manager_id=pk)
    msg1=""   
    context={'man':man,'msg1':msg1}
    if(request.method=="POST"):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pword = request.POST.get('pword')
        phone_no = request.POST.get('phone')
        if(fname != None and lname !=None and email != None  and pword != None and phone_no != None ):
            Manager.objects.filter(manager_id=man.manager_id).update(pword=pword, first_name=fname, last_name=lname, email=email, phone_number=phone_no)
            return redirect('manager_page',pk=man.manager_id)
        else:
            msg1 = "Details filled incorrectly"
            return render(request,'base/update_man.html',context)
     
    return render(request,'base/update_man.html',context)

def booking(request,cust,hotel,room):
    msg1=""
    cus = Customer.objects.get(cust_id=cust)
    hot = Hotel.objects.get(hotel_id=hotel)
    room = Room.objects.get(room_id=room)
    res = Reservation.objects.all() #get(room_id=room.room_id)
    now = datetime.now().date
    context={"msg1":msg1,'hotel':hot,'room':room, 'cus':cus,'res':res,'now':now}
    if (request.method=="POST"):
        start = request.POST.get('start')
        end = request.POST.get('end')
        if(start != None and end != None):
            abhi = str(datetime.now().date())
            if(end<=start or start<abhi):
                return render (request,'base/booking.html',context)
            for r in res:
                print(str(r.checkout.date()))
                print(start)
                if(str(r.checkout.date())>start and r.room_id==room.room_id):
                    return render (request,'base/booking.html',context)
            now = datetime.now()
            now = now.strftime("%H:%M:%S")
            hey = Reservation.objects.create(room_id=room.room_id,room_no=room.room_no, hotel_id=hotel, cust=cus,reser_time=now, checkout=end, checkin=start)
            hey.save()
            room.available="NO"
            room.save()
            return redirect('hotel', pk=cust)
    return render (request,'base/booking.html',context)