# serializers.py

from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Habit
        fields = '__all__'