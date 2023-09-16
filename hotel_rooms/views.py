from django.shortcuts import render

from . import defs_for_room_correct_reservation


def reservation_room(request):
    return defs_for_room_correct_reservation.reserve_room(request)


def reserve_room_data(request):
    return defs_for_room_correct_reservation.reserve_room_data(request)


def success(request):
    return render(request, 'hotel_rooms/success_room_reservation.html')
