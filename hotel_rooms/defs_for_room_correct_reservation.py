from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from myexceptions.my_exceptions import DateWrongType
from .models import *
from .send_success_email import send_confirmation_email
from django.contrib.auth.decorators import login_required


def reserve_room(request):
    room_types = Room.objects.all()
    room_options = RoomOption.objects.all()
    is_authenticated = request.user.is_authenticated
    request.session['reserve_room_redirect'] = request.get_full_path()
    return render(request, 'hotel_rooms/reservation_hotel_room.html',
                  {'room_types': room_types, 'room_options': room_options, 'is_authenticated': is_authenticated})


def reserve_room_data(request):
    if request.method == 'POST':
        try:
            full_name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            room_type_id = request.POST.get('room-type')
            room_option_id = request.POST.get('room-option')
            check_in_date = request.POST.get('check-in')
            check_out_date = request.POST.get('check-out')
            promo_code = request.POST.get('promo-code')
            additional_message = request.POST.get('message')

            price = calculate_price(room_type_id, room_option_id, check_in_date, check_out_date, promo_code)

            reserved_room = ReservedRoom(
                full_name=full_name,
                phone=phone,
                email=email,
                type_id=room_type_id,
                option_id=room_option_id,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                price=price,
                promo_code=promo_code,
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


def calculate_price(room_type_id, room_option_id, check_in_date, check_out_date, promo_code):
    room_type = Room.objects.get(pk=room_type_id)
    room_type_pr = room_type.default_price
    room_opt = RoomOption.objects.get(pk=room_option_id)
    room_opt_pr = room_opt.ind

    date_delta = reserved_days_qty(check_in_date, check_out_date)

    price = (room_type_pr + room_opt_pr) * date_delta

    if promo_code.lower() in promo_codes_list_10:
        price -= price // 10
    elif promo_code.lower() in promo_codes_list_5:
        price -= price // 20
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


promo_codes_list_10 = ['python', 'django', 'hotel', 'promo10', 'pr10omo', 'python2023']
promo_codes_list_5 = ['django2023', 'bakart_hotel', 'promo05', 'pr05omo', 'pyt2023']
