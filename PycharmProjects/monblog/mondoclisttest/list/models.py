from django.db import models

# Create your models here.
from django.http import HttpResponse


class Collection(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField()

    @classmethod
    def get_default_collection(cls) -> "Collection":
        collection, created = cls.objects.get_or_create(name="Defaut", slug="_defaut")

        return collection

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=350)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.description



