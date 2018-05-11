from django.conf import settings

REGISTER_DJANGO_DB_LOCK_ADMIN = getattr(settings, "REGISTER_DJANGO_DB_LOCK_ADMIN", False)
ENABLE_DJANGO_DB_LOCK_CSRF_PROTECT = getattr(settings, "ENABLE_DJANGO_DB_LOCK_CSRF_PROTECT", False)
