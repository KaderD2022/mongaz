from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Commande
from django.contrib.auth.decorators import login_required
from gaz.models import Gaz

# Create your views here.

def index(request):
    products = Gaz.objects.all()
    new_products = Gaz.objects.all()
    return render(request, 'gaz/index.html', {'products': products,
                                             'new_products': new_products})


@login_required
def detailnew(request, slug: str):
    products = get_object_or_404(Gaz, slug=slug)
    return render(request, 'gaz/detail.html', {'product': products})

@login_required
def order(request):
    orders = get_object_or_404(Commande)
    return render(request, 'gaz/commande.html', {'orders': orders})



@login_required
def enregistrer_commande(request):
    if request.method == 'POST':
        # récupérer les données de commande à partir du POST
        # créez une nouvelle commande et enregistrez-la dans la base de données
        commande = Commande.objects.create(
            users=request.user,
            quantite=request.POST.get('quantite'),
            numero=request.POST.get('numero'),
            adresse_livraison=request.POST.get('adresse_livraison'),
            date_livraison=request.POST.get('date_livraison')
        )
        # rediriger l'utilisateur vers la page de confirmation de commande
        return redirect('confirmation_commande', commande_id=commande.id)
    else:
        # si la méthode HTTP n'est pas POST, afficher une page de commande avec le formulaire
        return render(request, 'gaz/com.html')
