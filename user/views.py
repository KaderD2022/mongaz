

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from gaz.models import Gaz


from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    products = Gaz.objects.all()
    context={
        'products': products,
    }
    return render(request, 'user/index.html', context)



@login_required
def detail(request, slug: str):
    products = get_object_or_404(Gaz, slug=slug)
    return render(request, 'user/detail.html', {'product': products})


def my_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
               
                return redirect('home')
               
            else:
                messages.error(request, "Vous etez pas encore client")
                return render(request, 'gaz/login.html', {})
        else:
            return render(request, 'user/login.html', {})

    else:
        return redirect('home')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        first_name = request.POST['first_name']
        print(first_name)
        last_name = request.POST['last_name']
        print(last_name)
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
        user = User(username=username, first_name=first_name, last_name=last_name, email=email,
          password=password)
        print(user)
        user.save()
        print('Valideeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')      
        return render(request, 'user/register.html', {'user': user})
    else:
        print('non validesssssssssssssssssssssssssssssssssssssssssssssssssss')
        return render(request, 'user/register.html', )


