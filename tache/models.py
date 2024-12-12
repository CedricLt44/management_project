import uuid

from django.db import models

from account.models import User
from projet.models import Project
from todolist.models import Todolist
# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='tasks',on_delete = models.CASCADE)
    todolist = models.ForeignKey(Todolist,related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField( blank=True, null=True)
    is_done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='tasks', on_delete = models.CASCADE)

    def __str__(self):
      return self.name
