from django.shortcuts import render

from . import defs_for_correct_registration

from .models import Room


def index(request):
    rooms = Room.objects.all()
    return render(request, 'homepage.html', {'rooms': rooms})


def about_us(request):
    return render(request, 'about.html')


def registrate(request):
    return defs_for_correct_registration.registrate(request)


def success(request):
    return defs_for_correct_registration.success(request)


def reserve(request):
    return defs_for_correct_registration.reserve(request)
