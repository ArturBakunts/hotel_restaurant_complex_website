from django.shortcuts import render, redirect

from . import def_for_first_config


def index(request):
    return render(request, 'first_visit_page.html')


def upload_data(request):
    def_for_first_config.create_models()
    return redirect('homepage')
