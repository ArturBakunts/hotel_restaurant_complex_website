from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='homepage'),
               path('reservate/', views.reservation_room, name='reservation_room'),
               path('about/', views.about_us, name='about'),
               path('reserve/room/', views.reserve_room_data, name='reservation_room_data'),
               path('success/', views.success, name='success_room_reservation_page'),
               ]
