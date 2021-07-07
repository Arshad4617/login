from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm, CreateUserForm
# Create your views here.


def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_view')
    context = {}
    return render(request, 'base.html', context)


def create_new(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"User Account created Successfully " + user )
            return redirect('/')
    return render(request, "pages/new_account.html", {"form": form})


def forgot_pass(request):
    password = request.POST.get('password')

    # if request.method == 'POST':
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        #
        # user =
    context = {
        password:"password"
    }
    return render(request, "pages/forgot_pass.html", password)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "register.html", {"form": form})

def home_view(request):
    return render(request, "home.html")
