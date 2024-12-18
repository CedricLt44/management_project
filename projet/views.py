from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProjectFileForm
from .models import Project, ProjectNote
from gestion_client.models import Customer, Invoice

# Create your views here.
@login_required
def projects (request):
  projects = Project.objects.filter(created_by=request.user).select_related('customer')
  return render(request, 'projet/projets.html',{
    'projects': projects
    })


@login_required
def project(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    return render(request, 'projet/projet.html', {
        'project': project
    })

@login_required
def add(request):
  customers = Customer.objects.filter(created_by=request.user)
  if request.method == 'POST':
    name = request.POST.get('name', '')
    description = request.POST.get('description', '')
    customer_id = request.POST.get('customer')

    if name and customer_id :
      
        customer = Customer.objects.get(id=customer_id)

        Project.objects.create(name=name, description=description, created_by=request.user, customer=customer)

        return redirect('/projets/')
    else:
      print('Non valide')

  return render(request, 'projet/add.html',{
     'customers': customers
  }
                
                )

@login_required
def edit(request, pk):
  
  project = Project.objects.filter(created_by=request.user).get(pk=pk)
  customers = Customer.objects.filter(created_by=request.user)

  invoice = Invoice.objects.filter(customer=project.customer, total=project.price).first()


  if request.method == 'POST':
    name = request.POST.get('name', '')
    description = request.POST.get('description', '')
    customer_id = request.POST.get('customer', '')
    price =request.POST.get('price', None)
    invoice_comment = request.POST.get('invoice_comment', '')

    if name:
        project.name = name
        project.description = description
        project.customer = Customer.objects.get(id=customer_id)

        
        if price is not None :
            project.price = price
            project.save()
            
            if invoice:
                invoice.comment = invoice_comment 
                invoice.total =price
                invoice.save()
            else:
                invoice = Invoice(
                customer=project.customer,
                created_by=request.user,
                total=project.price,
                invoice_type='P',
                comment=invoice_comment
                )
                invoice.save()

            return redirect('/projets/')
      
  return render(request, 'projet/edit.html', {
        'project': project,
        'customers': customers,
        'invoice': invoice
    })

@login_required
def delete(request, pk):
   project = Project.objects.filter(created_by=request.user).get(pk=pk)
   project.delete()

   return redirect('/projets/')


# Création des vues permettant de upload des fichier 
# pour chaque projet

@login_required
def upload_file(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)

    if request.method == 'POST':
      form =ProjectFileForm(request.POST, request.FILES)
      
      if form.is_valid():
         projectfile = form.save(commit=False)
         projectfile.project = project
         projectfile.save()

         return redirect(f'/projets/{project_id}/')
    else:
        form = ProjectFileForm()

    return render(request, 'projet/upload_file.html', {
       'project':project,
       'form':form
    })

@login_required
def delete_file(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    projectfile = project.files.get(pk=pk)
    projectfile.delete()

    return redirect(f'/projets/{project_id}/')

# Création des vues pour l'ajout de notes d'un projet

@login_required
def add_note(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        body = request.POST.get('body', '')

        if name and body:
            ProjectNote.objects.create(
                project=project,
                name=name,
                body=body
            )

            return redirect(f'/projets/{project_id}/')

    return render(request, 'projet/add_note.html', {
        'project': project
    })

@login_required
def note_detail(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    note = project.notes.get(pk=pk)

    return render(request, 'projet/note_detail.html', {
        'project': project,
        'note': note
    })


@login_required
def note_edit(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    note = project.notes.get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        body = request.POST.get('body', '')

        if name and body:
           note.name = name
           note.body = body
           note.save()

           return redirect(f'/projets/{project_id}/')

    return render(request, 'projet/note_edit.html', {
        'project': project,
        'note': note
    })


@login_required
def note_delete(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    note = project.notes.get(pk=pk)
    note.delete()

    return redirect(f'/projets/{project_id}/')