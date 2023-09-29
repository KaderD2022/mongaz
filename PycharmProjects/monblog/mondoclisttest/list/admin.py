from django.contrib import admin

# Register your models here.
from list.models import Task, Collection

admin.site.register(Collection)
admin.site.register(Task)
