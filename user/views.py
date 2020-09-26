from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class Login(View):
    template_name = "auth/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("index")

        return render(request, self.template_name, {})

    def post(self, request):
        username: str = request.POST.get("username")
        password: str = request.POST.get("password")

        user: User or None = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("index")

        messages.error(request, "Nie znam takiego usera :P")
        return redirect("login")


def logout_view(request):
    logout(request)
    return redirect("index")
