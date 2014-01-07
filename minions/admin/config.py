from django.core.urlresolvers import reverse_lazy
APP_ADMIN_URLS = {
    'url_base': 'brukere',
    'namespace': 'users',
}
APP_ADMIN_MENU = {
    'Brukere': {
        'Oversikt': {
            'url': reverse_lazy('admin:users:list'),
            'icon': 'icon-th-list',
            'order': 0,
        },
        'Legg til': {
            'url': reverse_lazy('admin:users:create'),
            'icon': 'icon-plus-sign',
            'order': 1,
        },
    }
}
