from django.shortcuts import render
from django.views import generic
from .models import User


class UserListView(generic.ListView):
    queryset = User.objects.all()
    template_name = 'index.html'
