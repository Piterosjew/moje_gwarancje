from django.urls import path

from product.views import AddView, ProductListView, EditProductView

app_name = "product"

urlpatterns = [
    path("new", AddView.as_view(), name="new"),
    path("list", ProductListView.as_view(), name="list"),

    # pk - primary key, czyli identyfikator produktu
    path("edit/<pk>", EditProductView.as_view(), name="edit"),
]
