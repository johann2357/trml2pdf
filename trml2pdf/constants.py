from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

fonts_location = getattr(settings, 'FONTS_DIR', None)
if not fonts_location:
    raise ImproperlyConfigured(
        'There is no FONTS_DIR variable in your settings.py'
    )
