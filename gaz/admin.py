from django.contrib import admin

from gaz.models import Gaz, NewGaz, Commande

# Register your models here.
class AdminGaz(admin.ModelAdmin):
    list_display = ('title', 'description','color','company','price','type','number_register')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('company', 'title', 'type')
    ordering = ('type', 'number_register')
    filter = ('number_register', 'company')
    list_filter = ('number_register', 'company')
    
class AdminNewGaz(admin.ModelAdmin):
    list_display = ('title', 'description','color','company','price','type','number_register')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('company', 'title', 'type')
    ordering = ('type', 'number_register')
    filter = ('number_register', 'company')
    list_filter = ('number_register', 'company')
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('users', 'gaz', 'newgaz','quantite','numero','adresse_livraison','date_livraison','date_commande')
    search_fields = ('users', 'numero', 'adresse_livraison')
    ordering = ('users', 'numero', 'adresse_livraison')
    filter = ('number_register', 'company')
    list_filter = ('users', 'numero')
    


admin.site.register(Gaz, AdminGaz)
admin.site.register(NewGaz, AdminNewGaz)
admin.site.register(Commande, AdminCommande)
