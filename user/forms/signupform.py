from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

from user.models import Profile
from web.horizontalformhelper import HorizontalFormHelper


class SignUpForm(UserCreationForm):
    username = UsernameField(label=_("Username"), widget=forms.TextInput(), )
    email = forms.EmailField(max_length=254, label="Email", widget=forms.EmailInput(), validators=[EmailValidator])

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper.add_submit("rejestruj")

    class Meta:
        model = Profile

        # @todo poszukać, w jaki sposób w django "zaimportować" klasę obiektu ze "stringa"?
        # model = settings.AUTH_USER_MODEL

        fields = ("username", "email", "password1", "password2")
