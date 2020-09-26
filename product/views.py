from django.views.generic import CreateView

from product.forms import ProductForm


class AddView(CreateView):
    template_name = "product/add.html"
    form_class = ProductForm
