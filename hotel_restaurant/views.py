from django.shortcuts import render, redirect
from . import defs_for_table_correct_reservation


def dining(request):
    return render(request, 'hotel_restaurant/reservation_table.html')


def reserve_table(request):
    return defs_for_table_correct_reservation.reserve_table(request)


def success_table_registration(request):
    return render(request, 'hotel_restaurant/table_registration_success_page.html')


