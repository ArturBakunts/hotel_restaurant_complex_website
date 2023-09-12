from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import ReservedTable


def dining(request):
    return render(request, 'hotel_restaurant/reservate_table.html')


def reserve_table(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            guest_qty = request.POST.get('guest_qty')
            reservation_date = request.POST.get('reservation_date')
            reservation_time = request.POST.get('reservation_time')

            reserved_table = ReservedTable(
                name=name,
                phone=phone,
                email=email,
                guest_qty=guest_qty,
                reservation_date=reservation_date,
                reservation_time=reservation_time
            )
            reserved_table.save()

            return redirect('success_table_registration_page')
        except Exception as ex:
            return HttpResponse(ex)


def success_table_registration(request):
    return render(request, 'hotel_restaurant/table_registration_success_page.html')