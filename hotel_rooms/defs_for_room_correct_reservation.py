from django.shortcuts import render, redirect

from myexceptions.my_exceptions import DateWrongType
from .models import *

from datetime import datetime

from .send_success_email import send_confirmation_email


def reserve_room(request):
    room_types = Room.objects.all()
    room_options = RoomOption.objects.all()
    return render(request, 'hotel_rooms/reservation_hotel_room.html',
                  {'room_types': room_types, 'room_options': room_options})


def reserve_room_data(request):
    if request.method == 'POST':
        try:
            full_name = request.POST.get('name')
            email = request.POST.get('email')
            room_type_id = request.POST.get('room-type')
            room_option_id = request.POST.get('room-option')
            check_in_date = request.POST.get('check-in')
            check_out_date = request.POST.get('check-out')
            additional_message = request.POST.get('message')
            price = calculate_price(room_type_id, room_option_id, check_in_date, check_out_date)

            reserved_room = ReservedRoom(
                full_name=full_name,
                email=email,
                type_id=room_type_id,
                option_id=room_option_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                price=price,
                additional_message=additional_message
            )

            if is_free_room(room_type_id):
                reserved_room.save()

                send_confirmation_email(
                    email=email,
                    name=full_name,
                    check_in=check_in_date,
                    check_out=check_out_date,
                    room_type=Room.objects.get(pk=room_type_id),
                    options_for_room=RoomOption.objects.get(pk=room_option_id),
                    price=price
                )

                return redirect('success_room_reservation_page')

            else:
                return render(request, 'hotel_rooms/no_free_rooms.html')
        except:
            return render(request, 'reservation_incorrect_date_type.html')


def calculate_price(room_type_id, room_option_id, check_in_date, check_out_date):
    room_type = Room.objects.get(pk=room_type_id)
    room_type_pr = room_type.default_price
    room_opt = RoomOption.objects.get(pk=room_option_id)
    room_opt_pr = room_opt.ind

    date_delta = reserved_days_qty(check_in_date, check_out_date)

    price = (room_type_pr + room_opt_pr) * date_delta

    return price


def is_free_room(room_type_id):
    room_type = Room.objects.get(pk=room_type_id)
    room_qty = room_type.free_room_qty
    if room_qty > 0:
        room_type.free_room_qty -= 1
        room_type.save()
        return True
    return False


def reserved_days_qty(check_in_date, check_out_date):
    date_in = datetime.strptime(check_in_date, '%Y-%m-%d').date()
    date_out = datetime.strptime(check_out_date, '%Y-%m-%d').date()
    date_now = datetime.now().date()
    if (date_in - date_now).days < 0 or (date_out - date_in).days < 1:
        raise DateWrongType
    date_delta = (date_out - date_in).days
    return date_delta



