from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from CustomUserApp.models import MyUser
from CustomUserApp.forms import LoginForm, RegisterForm
from CustomUserProject.settings import AUTH_USER_MODEL

def index_view(request):
    return render(request, "index.html", {"MyUser": MyUser.objects.all(), "AUTH_USER_MODEL": AUTH_USER_MODEL})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get("username"),
                display_name=data.get("display_name"),
                password=data.get("password"),
                age=data.get("age"),
                homepage=data.get("homepage"),
                )
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    
    form = RegisterForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))