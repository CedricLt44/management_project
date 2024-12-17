from django.urls import path

from . import views

app_name = 'gestion_client'

urlpatterns = [
    path('', views.customers, name='customers'),
    path('add/', views.add, name='add'),
    path('<int:id>/', views.customer, name='client'), # Vue pour afficher un client spécifique
]