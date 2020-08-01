from django.shortcuts import render
from django.views.generic import DetailView
from .models import Rover


class RoverProfileView(DetailView):
    model = Rover
    template_name = "rovers/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"