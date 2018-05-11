from django.conf import settings
from django.contrib import admin
from .models import Lock
from .settings import REGISTER_DJANGO_DB_LOCK_ADMIN

class LockAdmin(admin.ModelAdmin):
    list_display = ["lock_name", "worker_name", "lock_time", "expire_time"]
    search_fields = ["lock_name", "worker_name"]

if REGISTER_DJANGO_DB_LOCK_ADMIN:
    admin.site.register(Lock, LockAdmin)
