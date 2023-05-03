from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.ImageField(null=True, blank=True)


class Room(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    users = models.ManyToManyField(User, related_name='rooms')


class Desk(models.Model):
    title = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='desks')


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    desk = models.ForeignKey(Desk, on_delete=models.CASCADE, related_name='tasks')