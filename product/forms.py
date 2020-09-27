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
        self.user = user
        super(ProductForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        if not self.instance.owner:
            self.instance.owner = self.user
        # @todo do ogarnięcia błąd związany z edycją i dodawaniem nowego produktu w kontekście użytkownika
        # try:
        #     pass
        # except RelatedObjectDoesNotExist:
        #     pass
        return super(ProductForm, self).save(commit=commit)

    class Meta:
        model = Product
        fields = ("name", "shop", "bought_on", "warranty_date")
