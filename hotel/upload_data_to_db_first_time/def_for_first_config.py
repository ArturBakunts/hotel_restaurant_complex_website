from django.shortcuts import redirect, render

from hotel_restaurant.models import Table
from .data_for_db import room_type_list, room_option_list
from hotel_rooms.models import Room, RoomOption


def create_one_room_model(room_data):
    room = Room(
        title=room_data['title'],
        guests_qty=room_data['guests_qty'],
        price_optional=room_data['price_optional'],
        free_room_qty=room_data['free_room_qty'],
        default_price=room_data['default_price'],
        description=room_data['description'],
        image=f"room_images\{room_data['image']}"

    )
    room.save()


def create_one_room_option_model(option_data):
    room_option = RoomOption(
        title=option_data['title'],
        options=option_data['options'],
        ind=option_data['ind']
    )
    room_option.save()


def upload_data(request):
    create_models()
    return redirect('homepage')


def create_models():
    for room_type in room_type_list:
        create_one_room_model(room_type)

    for room_option in room_option_list:
        create_one_room_option_model(room_option)

    create_restaurant_table_model()


def create_restaurant_table_model():
    table = Table(
        guests_max_qty=4,
        free_tables_qty=25
    )
    table.save()
