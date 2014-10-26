from django.apps import AppConfig
from django.contrib.auth.models import User
try:
    from actstream import registry
except ImportError:
    pass
else:

    class MinionsAppConfig(AppConfig):
        name = 'minions'

        def ready(self):
            registry.register(User)
