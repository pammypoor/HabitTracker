from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HabitSerializer
from .models import Habit
from rest_framework.decorators import api_view

# Create your views here.
class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all().order_by('name')
    serializer_class = HabitSerializer
