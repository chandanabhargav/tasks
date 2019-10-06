from django.db import models
import datetime
from django.utils import timezone

class User(models.Model):
    userName = models.CharField(max_length = 50)
    password = models.TextField()


class Task(models.Model):
    userId = models.ForeignKey(User, on_delete = models.CASCADE)
    taskName = models.TextField()
    createdTime = models.DateTimeField(default=timezone.now)
    completionDate = models.DateTimeField()
    isDone = models.IntegerField()
