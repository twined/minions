# posts.py

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, ListView,
                                  UpdateView, DeleteView, FormView)

from django.contrib.auth.models import User

from minions.forms import UserForm, UserCreateForm, PassChangeForm
from minions.views import LoginRequiredMixin


class ListUsersView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "users"
    template_name = "users/admin/list.html"


class CreateUsersView(LoginRequiredMixin, CreateView):
    form_class = UserCreateForm
    template_name = "users/admin/create.html"
    success_url = reverse_lazy('admin:users:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        messages.success(self.request, "Success", extra_tags='msg')
        return super(CreateUsersView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(CreateUsersView, self).form_invalid(form)


class UpdateUsersView(LoginRequiredMixin, UpdateView):
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
        return super(UpdateUsersView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Rett feilene under")
        return super(UpdateUsersView, self).form_invalid(form)


class DeleteUsersView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/admin/user_confirm_delete.html"
    success_url = reverse_lazy('admin:users:list')


class ChangePasswordUsersView(LoginRequiredMixin, FormView):
    form_class = PassChangeForm
    template_name = "users/admin/change_password.html"
    success_url = reverse_lazy('admin:users:list')

    def get_form_kwargs(self):
        kwargs = super(ChangePasswordUsersView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        messages.success(self.request, "Endringen var vellykket.",
                         extra_tags='msg')
        form.save()
        return super(ChangePasswordUsersView, self).form_valid(form)
