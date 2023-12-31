from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import escape
from list.models import Collection, Task


def index(request):
    context = {}

    collection = Collection.get_default_collection()
    context["collections"] = Collection.objects.order_by("name")
    context["tasks"] = collection.task_set.order_by("description")

    return render(request, 'list/index.html', context=context)


def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, created = Collection.objects.get_or_create(name=collection_name)
    if created:
        return HttpResponse("La collection a été crée", status=409)
    else:
        return HttpResponse("La collection a déja été crée", status=409)

    return HttpResponse(f'<h2>{collection.name}<h2>')


def add_task(request):
    collection = Collection.get_default_collection()
    description = escape(request.POST.get("task-description"))
    Task.objects.create(description=description, collection=collection)
    return HttpResponse(description)