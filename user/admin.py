from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import   Client, Visiteur
# Register your models here.

class AdminVisiteur(admin.ModelAdmin):
    list_display = ('email', 'email')
    search_fields = ('email', 'email')
    ordering = ('email', 'email')
    filter = ('email', 'emal')
    list_filter = ('email', 'email')
    
class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    verbose_name_plural = 'client'

class UserAdmin(BaseUserAdmin):
    inlines = (ClientInline,)

class AdminClient(admin.ModelAdmin): 
    list_display = ('user', 'department','ville','address','geolocation','number')
    search_fields = ('vlle', 'address', 'number')
    ordering = ('user', 'number')
    filter = ('number', 'address')
    list_filter = ('number', 'ville')
    
    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Visiteur, AdminVisiteur)
admin.site.register(Client, AdminClient)

