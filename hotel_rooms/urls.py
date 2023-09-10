from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='homepage'),
               path('registrate/', views.registrate, name='registrate'),
               path('about/', views.about_us, name='about'),
               path('reserve/', views.reserve, name='reserve'),
               path('success/', views.success, name='success_page'),
               ]
