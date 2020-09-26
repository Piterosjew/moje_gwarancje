from django.urls import path

from product.views import AddView

app_name = "product"

urlpatterns = [
    path("new", AddView.as_view(), name="new"),
]
