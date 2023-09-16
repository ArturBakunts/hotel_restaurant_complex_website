from django.urls import path

from . import views

urlpatterns = [
    path('reservate/', views.reservation_room, name='reservation_room'),
    path('reserve/room/', views.reserve_room_data, name='reservation_room_data'),
    path('success/', views.success, name='success_room_reservation_page'),
]
