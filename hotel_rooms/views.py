from django.shortcuts import render, redirect

from . import defs_for_correct_reservation

from .models import Room


def index(request):
    rooms = Room.objects.all()
    if rooms:
        return render(request, 'hotel_rooms/index.html', {'rooms': rooms})
    else:
        return redirect('upload')


def about_us(request):
    return render(request, 'hotel_rooms/about.html')


def reservation_room(request):
    return defs_for_correct_reservation.reserve_room(request)


def reserve_room_data(request):
    return defs_for_correct_reservation.reserve_room_data(request)


def success(request):
    return defs_for_correct_reservation.success(request)
