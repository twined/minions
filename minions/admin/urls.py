from django.conf.urls import patterns, url
from minions.admin.views import (
    CreateUsersView, ListUsersView,
    DeleteUsersView, UpdateUsersView,
    ChangePasswordUsersView)

urlpatterns = patterns(
    '',
    url(r'^oversikt/$', ListUsersView.as_view(), name="list"),
    url(r'^ny/$', CreateUsersView.as_view(), name="create"),
    url(r'^slett/(?P<pk>\d+)/$', DeleteUsersView.as_view(), name="delete"),
    url(r'^endre/(?P<pk>\d+)/$', UpdateUsersView.as_view(), name="update"),
    url(r'^endre/(?P<pk>\d+)/password', ChangePasswordUsersView.as_view(),
        name="password"),
)
