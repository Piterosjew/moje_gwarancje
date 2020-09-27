from django.urls import path

from user.views import LoginView, logout_view, RegisterView, ChangePassword

app_name = "user"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
    path("register", RegisterView.as_view(), name="register"),
    path("change_password", ChangePassword.as_view(), name="change_password"),
]
