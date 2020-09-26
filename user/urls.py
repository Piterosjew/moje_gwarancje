from django.urls import path

from user.views import Login, logout_view

app_name = "user"

urlpatterns = [
    path("login", Login.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
]
