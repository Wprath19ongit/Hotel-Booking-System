from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home_page, name="home_page"),
    path('register/', views.register_page, name="register_page"),
    path('update_customer/<str:pk>', views.update_cust_page, name="update_cust_page"),
    path('update_manager/<str:pk>', views.update_man_page, name="update_man_page"),
    path('update_hotel/<str:pk>', views.update_hotel_page, name="update_hotel_page"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),
    path('manager/<str:pk>/', views.manager_page, name="manager_page"),
    path('hotel/<str:pk>/', views.hotel, name = "hotel"),
    path('booking/<str:cust>/<str:hotel>/<str:room>/', views.booking, name="booking"),
]
