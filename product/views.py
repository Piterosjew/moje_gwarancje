from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin as BaseLoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, FormView

from product.forms import ProductForm
from product.models import Product


class LoginRequiredMixin(BaseLoginRequiredMixin):
    def get_login_url(self):
        return reverse("user:login")


class AddView(LoginRequiredMixin, CreateView):
    template_name = "product/add.html"
    form_class = ProductForm

    def get_form(self, form_class=None):
        if self.request.POST:
            return self.form_class(self.request.user, self.request.POST)
        return self.form_class(self.request.user)

    def form_valid(self, form):
        form.save()
        return redirect(reverse('index'))


class ProductListView(LoginRequiredMixin, ListView):
    template_name = "product/list.html"
    model = Product

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class EditView(LoginRequiredMixin, FormView):
    pass


class EditProductView(LoginRequiredMixin, UpdateView):
    template_name = "product/add.html"
    form_class = ProductForm
    model = Product

    def get_form(self, form_class=None):
        return self.form_class(self.request.user, **self.get_form_kwargs())

    def get_success_url(self):
        messages.success(request=self.request, message="Produkt zaktualizowany")
        return reverse("product:list")
