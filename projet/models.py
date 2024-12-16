import uuid

from django.db import models

from account.models import User
from gestion_client.models import Customer
# Create your models here.

class Project(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=250)
  description = models.TextField( blank=True, null=True)
  created_by = models.ForeignKey(User, related_name='projects', on_delete = models.CASCADE)
  customer = models.ForeignKey(Customer, related_name='projects', on_delete=models.PROTECT, null=True, blank=True)
  price = models.DecimalField(max_digits=1000, decimal_places=2, null=True, blank=True)  # Prix du projet
  created_at = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.name
  

class ProjectFile(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
  name = models.CharField(max_length=250)
  attachment = models.FileField(upload_to='projectfiles')

  def __str__(self):
    return self.name
  
class ProjectNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='notes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name