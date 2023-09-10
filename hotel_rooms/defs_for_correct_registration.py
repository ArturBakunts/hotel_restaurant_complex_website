from django.shortcuts import render, redirect

from .models import *

from datetime import datetime

from .send_success_email import send_confirmation_email


def registrate(request):
    room_types = Room.objects.all()
    room_options = RoomOption.objects.all()
    return render(request, 'registrate.html', {'room_types': room_types, 'room_options': room_options})


def success(request):
    return render(request, 'success_page.html')


def incorrect_date_type(request):
    return render(request, 'incorrect_date_type.html')


def reserve(request):
    try:
        if request.method == 'POST':
            full_name = request.POST['name']
            email = request.POST['email']
            room_type_id = request.POST['room-type']
            room_option_id = request.POST['room-option']
            check_in_date = request.POST['check-in']
            check_out_date = request.POST['check-out']
            additional_message = request.POST['message']
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

                send_confirmation_email(email=email, name=full_name, check_in=check_in_date, check_out=check_out_date,
                                        room_type=Room.objects.get(pk=room_type_id),
                                        options_for_room=RoomOption.objects.get(pk=room_option_id), price=price
                                        )
                return redirect('success_page')
            else:
                return render(request, 'no_free_rooms.html')
    except:
        return incorrect_date_type(request)


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
        raise ValueError
    date_delta = (date_out - date_in).days
    return date_delta
