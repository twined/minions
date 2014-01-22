#models.py
import os
from django.contrib.auth.models import User
from django.db import models


def handle_profile_upload(instance, filename):
    _, ext = os.path.splitext(filename)
    return os.path.join(
        'images', 'avatars', str(instance.user.pk), 'avatar%s' % ext)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    avatar = models.ImageField(upload_to=handle_profile_upload,
                               blank=True, null=True)
