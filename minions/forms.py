# forms.py

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm


class UserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Send inn'))
        super(UserForm, self).__init__(*args, **kwargs)


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Send inn'))
        super(UserCreateForm, self).__init__(*args, **kwargs)


class PassChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Send inn'))
        super(PassChangeForm, self).__init__(*args, **kwargs)
