from django.shortcuts import render, redirect

from hotel_rooms.models import Room


def index(request):
    rooms = Room.objects.all()
    if rooms:
        return render(request, 'hotel/index.html', {'rooms': rooms})
    else:
        return redirect('upload')


def about_us(request):
    return render(request, 'hotel/about.html')


def registrate_user(request):
    return render(request, 'hotel/user_registration.html')


def login_user(request):
    return render(request, 'hotel/user_login.html')
