# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.core.files.images import get_image_dimensions

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UserProfile


class UserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Lagre'))
        super(UserForm, self).__init__(*args, **kwargs)


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Lagre'))
        super(UserCreateForm, self).__init__(*args, **kwargs)


class PassChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Lagre'))
        super(PassChangeForm, self).__init__(*args, **kwargs)


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Lagre'))
        super(UserProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserProfile
        exclude = ['user']

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            #validate dimensions
            max_width = max_height = 200
            if w != max_width or h != max_height:
                raise forms.ValidationError(
                    u'Vennligst bruk et bilde som er '
                    '%s x %s pixler.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'jpg', 'gif', 'png']):
                raise forms.ValidationError(
                    u'Kun JPEG, '
                    'GIF eller PNG format.')

            #validate file size
            if len(avatar) > (100 * 1024):
                raise forms.ValidationError(
                    u'Max størrelse er 100k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar
