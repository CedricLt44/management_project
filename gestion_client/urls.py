from django.urls import path

from . import views

app_name = 'gestion_client'

urlpatterns = [
  path('' ,views.gestion_client, name='gestion_client'),
  ]