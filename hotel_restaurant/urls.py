from django.urls import path

from . import views

urlpatterns = [path('reserve/table/', views.reserve_table, name='reserve_table'),
               path('dining/', views.dining, name='dining'),
               path('success/', views.success_table_registration, name='success_table_registration_page'),
               ]
