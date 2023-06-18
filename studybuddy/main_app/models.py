from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=100)


class Study_Group(models.Model):
  # Storing location as coordinates so we can display with GMaps
  location = models.CharField(max_length=100)
  topic = models.CharField(max_length=100)
  school = models.ForeignKey(School, on_delete=models.CASCADE)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  study_groups = models.ManyToManyField(Study_Group)

# Make sure to add credit to tutorial
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()

