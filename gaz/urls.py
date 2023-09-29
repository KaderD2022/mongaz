from django.urls import path
from gaz.views import index, detailnew, enregistrer_commande, order


urlpatterns = [
    path('', index, name="home"),
    path('detailnew/<slug>/',  detailnew, name="detailnew"),
    path('order/',  order, name="order"),
    path('commande/',  enregistrer_commande, name="commande"),
]
