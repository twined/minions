# -*- coding: utf-8 -*-
"""
// twined - minions
// admin views definitions for the minions app
// (c) Twined/Univers 2009-2014. All rights reserved.
"""

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import ListView

from minions.forms import PassChangeForm
from minions.forms import UserCreateForm
from minions.forms import UserForm
from minions.forms import UserProfileForm
from minions.models import UserProfile
from minions.views import LoginRequiredMixin


class UsersListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "users"
    template_name = "users/admin/list.html"


class UsersCreateView(LoginRequiredMixin, CreateView):
    form_class = UserCreateForm
    template_name = "users/admin/create.html"
    success_url = reverse_lazy('admin:users:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, "Success", extra_tags='msg')
        return super(UsersCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(UsersCreateView, self).form_invalid(form)


class UsersUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/admin/update.html"
    success_url = reverse_lazy('admin:users:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # set the owner to be the current user
        self.object.user = self.request.user
        messages.success(self.request, "Endringen var vellykket.",
                         extra_tags='msg')
        return super(UsersUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(UsersUpdateView, self).form_invalid(form)


class UsersDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/admin/user_confirm_delete.html"
    success_url = reverse_lazy('admin:users:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # set the owner to be the current user
        messages.success(self.request, "Endringen var vellykket.",
                         extra_tags='msg')
        return super(UsersUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(UsersUpdateView, self).form_invalid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "users/admin/profile.html"
    success_url = reverse_lazy('admin:dashboard')

    def get_object(self):
        usr, created = UserProfile.objects.get_or_create(
            user__pk=self.request.user.id,
            defaults={'user': self.request.user})
        return usr

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # set the owner to be the current user
        self.object.user = self.request.user
        messages.success(self.request, "Endringen var vellykket.",
                         extra_tags='msg')
        return super(ProfileUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(ProfileUpdateView, self).form_invalid(form)


class PasswordChangeView(LoginRequiredMixin, FormView):
    form_class = PassChangeForm
    template_name = "users/admin/change_password.html"
    success_url = reverse_lazy('admin:users:list')

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        messages.success(self.request, "Endringen var vellykket.",
                         extra_tags='msg')
        form.save()
        return super(PasswordChangeView, self).form_valid(form)
