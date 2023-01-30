from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isComplete = models.BooleanField()
    created_by = models.OneToOneField(User,  on_delete=models.CASCADE, primary_key=True)
    start_date = models.DateField(blank=False, null=True)
    end_date = models.DateField(blank=False, null=True)

    def __str__(self):
        return self.name

    def save_model(self, request, obj, form, change): 
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

