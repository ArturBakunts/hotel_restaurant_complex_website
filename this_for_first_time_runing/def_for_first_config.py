from django.shortcuts import redirect

from .data_for_db import room_type_list, room_option_list
from hotel_rooms.models import Room, RoomOption
import os
from django.core.files import File
import subprocess


# def run_migrations():
#     try:
#         subprocess.run(['python', 'manage.py', 'makemigrations'])
#
#         subprocess.run(['python', 'manage.py', 'migrate'])
#     except Exception as e:
#         print(f"An error occurred: {e}")


def create_one_room_model(room_data):
    image_filename = room_data['image']
    image_path = os.path.join('media', 'room_images', image_filename)

    room = Room(
        title=room_data['title'],
        guests_qty=room_data['guests_qty'],
        price_optional=room_data['price_optional'],
        free_room_qty=room_data['free_room_qty'],
        default_price=room_data['default_price'],
        description=room_data['description']
    )

    with open(image_path, 'rb') as img_file:
        room.image.save(image_filename, File(img_file), save=True)


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
    # run_migrations()

    for room_type in room_type_list:
        create_one_room_model(room_type)

    for room_option in room_option_list:
        create_one_room_option_model(room_option)
