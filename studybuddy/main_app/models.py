from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)


class Topic(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Study_Group(models.Model):
    # Storing location as coordinates so we can display with GMaps
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    creator = models.ForeignKey(
        User, related_name='creator', on_delete=models.CASCADE)
    attending = models.ManyToManyField(User, related_name='attending')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

# Credit for extending the user profile to this tutorial: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        default = School.objects.get(pk=3)
        Profile.objects.create(user=instance, school=default)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
