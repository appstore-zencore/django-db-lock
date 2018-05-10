from django.urls import path
from .views import acquire_lock
from .views import release_lock
from .views import get_lock_info
from .views import clear_expired_locks

urlpatterns = [
    path('acquire-lock', acquire_lock, name="django_db_lock.acquire_lock"),
    path('release-lock', release_lock, name="django_db_lock.release_lock"),
    path('get-lock-info', get_lock_info, name="django_db_lock.get_lock_info"),
    path('clear-expired-locks', clear_expired_locks, name="django_db_lock.clear_expired_locks"),
]
