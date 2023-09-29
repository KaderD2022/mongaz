from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse("You did it this time!,"),
    #return render(request, 'blog/index.html'),


