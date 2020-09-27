from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name=_("Product name"))
    shop = models.CharField(max_length=250, blank=False, null=False)
    bought_on = models.DateField(null=False, blank=False)
    warranty_date = models.DateField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
