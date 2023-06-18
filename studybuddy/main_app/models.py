from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Study_Group(models.Model):
  # Storing location as coordinates so we can display with GMaps
  location = models.CharField(max_length=100)
  topic = models.CharField(max_length=100)
  attending = models.ForeignKey(User, on_delete=models.CASCADE)

class School(models.Model):
  name = models.CharField(max_length=100)
  study_groups = models.ForeignKey(Study_Group, on_delete=models.CASCADE)
  students = models.ForeignKey(User, on_delete=models.CASCADE)