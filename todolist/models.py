import uuid

from django.db import models

from account.models import User
from projet.models import Project
# Create your models here.

class Todolist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='todolists',on_delete = models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField( blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def completed_tasks_count(self):
        # Utilisation du related_name défini dans le modèle Task
        return self.tasks.filter(is_done=True).count()

    def total_tasks_count(self):
        # Utilisation du related_name défini dans le modèle Task
        return self.tasks.count()

    def __str__(self):
      return self.name
