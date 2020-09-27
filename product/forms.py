from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        label="name",
        max_length=100,
        help_text="Podaj nazwę produktu",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg pr-4 shadow-none"})
    )
    bought_on = forms.DateField(
        label="Bought on data",
        widget=forms.DateInput(attrs={"class": "form-control form-control-lg pr-4 shadow-none"})
    )

    def __init__(self, user, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = ("name", "shop", "bought_on", "warranty_date")
