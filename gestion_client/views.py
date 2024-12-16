from django.shortcuts import render

# Définition de la vue
def gestion_client(request):
    return render(request, 'gestion_client/gestion_client.html')
