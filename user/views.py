from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class Index(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name, {})


class Login(View):
    template_name = "auth/login.html"

    def get(self, request):
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
