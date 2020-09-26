from django.urls import path

from user.views import Login, Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("login", Login.as_view(), name="login"),
]
