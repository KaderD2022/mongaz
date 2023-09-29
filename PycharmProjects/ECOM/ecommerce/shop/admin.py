from django.contrib import admin

from .models import Category, Product, Commande
admin.site.site_header = "E-COMMERCE"
admin.site.site_title = "SBC shop"
admin.site.index_title = "MANAGER"


class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'date_added')
    search_fields = ("title",)
    list_editable = ('price',)



class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays', 'zipcode', 'total', 'date_commande')


admin.site.register(Category, AdminCategorie)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)
