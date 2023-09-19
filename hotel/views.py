from django.db import IntegrityError
from django.shortcuts import render, redirect

from myexceptions.my_exceptions import PasswordConfirmError
from .models import MyUser
from hotel_rooms.models import Room
from django.contrib.auth.models import User


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


def registration_user_data(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            phone_number = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm = request.POST.get('confirm')
            country = request.POST.get('country')
            passport_id = request.POST.get('passport')
            bank_card_number = request.POST.get('card')
            expiration_date = request.POST.get('expiration')
            cvv = request.POST.get('cvv')

            if password != confirm:
                raise PasswordConfirmError

            user = User.objects.create_user(
                username=email,
                password=password,
                email=email,
                first_name=name,
                last_name=surname
            )

            my_user = MyUser.objects.create(
                user=user,
                phone_number=phone_number,
                country=country,
                passport_id=passport_id,
                bank_card_number=bank_card_number,
                expiration_date=expiration_date,
                cvv=cvv

            )
            return redirect('success_user_reservation_page')

        except IntegrityError:
            error_message = 'A user with the email address you provided already exists. Please use a different email'

        except PasswordConfirmError:
            error_message = "Password and Confirm Password do not match."

        return render(request, 'hotel/user_registration_failed.html', {'error_message': error_message})


def success_user_reservation(request):
    return render(request, 'hotel/success_user_registration.html')
