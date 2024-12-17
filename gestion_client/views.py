from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Customer, Invoice

# Définition de la vue pour afficher les clients
@login_required
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'gestion_client/gestion_client.html', {
        'customers': customers
    })

@login_required
def customer(request, id):
        
    customer = Customer.objects.get( id=id,)
    return render(request, 'gestion_client/client.html', {
        'customer': customer
    })
# Définition de la vue pour ajouter un client
@login_required
def add(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        name = request.POST.get('name', '')
        contact_name = request.POST.get('contact_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')

        # Vérification que le nom est fourni avant de créer l'objet
        if name:
            # Création d'un nouveau client associé à l'utilisateur connecté
            Customer.objects.create(
                name=name,
                contact_name=contact_name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                zip_code=zip_code,
                created_by=request.user  # Associe l'utilisateur connecté au client
            )
            return redirect('/gestion_client/')  # Redirection après la création
        else:
            print('Le nom est obligatoire')
            # Si le nom est vide, afficher un message d'erreur ou rediriger

    return render(request, 'gestion_client/add.html')
