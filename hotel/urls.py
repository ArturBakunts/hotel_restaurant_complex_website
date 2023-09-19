from django.urls import path
from . import views
from .upload_data_to_db_first_time import def_for_first_config

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about/', views.about_us, name='about'),
    path('success/user/registration', views.success_user_reservation, name='success_user_reservation_page'),
    path('upload/data/', def_for_first_config.upload_data, name='upload'),
    path('user/registration/', views.registrate_user, name='registration'),
    path('user/registration/data', views.registration_user_data, name='registration_user_data'),
    path('user/login/', views.login_user, name='login'),

]

