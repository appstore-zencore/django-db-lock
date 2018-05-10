from django.conf import settings
from django.contrib import admin
from .models import Lock

class LockAdmin(admin.ModelAdmin):
    list_display = ["lock_name", "worker_name", "lock_time", "expire_time"]
    search_fields = ["lock_name", "worker_name"]

if getattr(settings, "REGISTER_DJANGO_DB_LOCK_ADMIN", False):
    admin.site.register(Lock, LockAdmin)
