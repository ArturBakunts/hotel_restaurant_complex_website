from django.shortcuts import redirect, render
from datetime import datetime
from myexceptions.my_exceptions import DateWrongType
from .models import ReservedTable, Table


def reserve_table(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            guest_qty = int(request.POST.get('guest_qty'))
            reservation_date = request.POST.get('reservation_date')
            reservation_time = request.POST.get('reservation_time')
            table_type = Table.objects.all()[0]

            reserved_table = ReservedTable(
                name=name,
                phone=phone,
                email=email,
                guest_qty=guest_qty,
                reservation_date=reservation_date,
                reservation_time=reservation_time,
                table_type=table_type
            )

            if not check_correct_datetime(reservation_date, reservation_time):
                raise DateWrongType
            if not correct_guests_qty(table_type, guest_qty):
                return render(request, 'hotel_restaurant/wrong_qty_for_guests.html')

            if not is_free_table(table_type):
                return render(request, 'hotel_restaurant/no_free_tables.html')

            reserved_table.save()

            return redirect('success_table_registration_page')
        except:
            return render(request, 'reservation_incorrect_date_type.html')


def correct_guests_qty(table_object, guest_qty):
    return table_object.guests_max_qty >= guest_qty


def is_free_table(table_object):
    if table_object.free_tables_qty > 0:
        table_object.free_tables_qty -= 1
        table_object.save()
        return True
    return False


def check_correct_datetime(reservation_date, reservation_time):
    reservation_datetime_str = f'{reservation_date} {reservation_time}'
    reservation_datetime = datetime.strptime(reservation_datetime_str, '%Y-%m-%d %H:%M')
    time_delta = (reservation_datetime - datetime.now()).total_seconds()
    return time_delta > 0
