from django.shortcuts import render
from django.views import generic
from .models import User


class UserListView(generic.ListView):
    model = User
    context_object_name = 'users'
    queryset = User.objects.all()
    template_name = 'allusers.html'
