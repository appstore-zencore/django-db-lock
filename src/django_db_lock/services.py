import datetime
from django.utils.timezone import now
from django.db.utils import IntegrityError
from django.db import transaction
from .models import Lock


def clear_expired_locks():
    now_time = now()
    with transaction.atomic():
        Lock.objects.filter(expire_time__lte=now_time).delete()


def acquire_lock(lock_name, worker_name, timeout):
    clear_expired_locks()
    lock = Lock()
    lock.lock_name = lock_name
    lock.worker_name = worker_name
    lock.lock_time = now()
    lock.expire_time = lock.lock_time + datetime.timedelta(seconds=timeout)
    try:
        with transaction.atomic():
            lock.save()
        return True
    except IntegrityError:
        return False


def release_lock(lock_name, worker_name):
    clear_expired_locks()
    try:
        lock = Lock.objects.get(lock_name=lock_name, worker_name=worker_name)
        with transaction.atomic():
            lock.delete()
        return True
    except Lock.DoesNotExist:
        return True
    return False


def get_lock_info(lock_name):
    try:
        lock = Lock.objects.get(lock_name=lock_name)
        return {
            "pk": lock.pk,
            "lock_name": lock.lock_name,
            "worker_name": lock.worker_name,
            "lock_time": lock.lock_time,
            "expire_time": lock.expire_time,
        }
    except Lock.DoesNotExist:
        return None
