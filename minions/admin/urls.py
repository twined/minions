from django.conf.urls import patterns, url
from minions.admin.views import (
    UsersCreateView, UsersListView,
    UsersDeleteView, UsersUpdateView,
    PasswordChangeView,
    ProfileUpdateView)

urlpatterns = patterns(
    '',
    url(r'^profil/$', ProfileUpdateView.as_view(), name="profile"),
    url(r'^oversikt/$', UsersListView.as_view(), name="list"),
    url(r'^ny/$', UsersCreateView.as_view(), name="create"),
    url(r'^slett/(?P<pk>\d+)/$', UsersDeleteView.as_view(), name="delete"),
    url(r'^endre/(?P<pk>\d+)/$', UsersUpdateView.as_view(), name="update"),
    url(r'^endre/(?P<pk>\d+)/password', PasswordChangeView.as_view(),
        name="password"),
)
