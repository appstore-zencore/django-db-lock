from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .settings import ENABLE_DJANGO_DB_LOCK_CSRF_PROTECT
from .services import acquire_lock as do_acquire_lock
from .services import release_lock as do_release_lock
from .services import get_lock_info as do_get_lock_info
from .services import clear_expired_locks as do_clear_expired_locks


def acquire_lock(request):
    lock_name = request.POST.get("lock_name")
    worker_name = request.POST.get("worker_name")
    timeout = int(request.POST.get("timeout"))
    result = do_acquire_lock(lock_name, worker_name, timeout)
    return JsonResponse({
        "result": result,
    })

def release_lock(request):
    lock_name = request.POST.get("lock_name")
    worker_name = request.POST.get("worker_name")
    result = do_release_lock(lock_name, worker_name)
    return JsonResponse({
        "result": result,
    })

def get_lock_info(request):
    lock_name = request.GET.get("lock_name")
    info = do_get_lock_info(lock_name)
    return JsonResponse({
        "result": info,
    })

def clear_expired_locks(request):
    do_clear_expired_locks()
    return JsonResponse({
        "result": True
    })


if not ENABLE_DJANGO_DB_LOCK_CSRF_PROTECT:
    acquire_lock = csrf_exempt(acquire_lock)
    release_lock = csrf_exempt(release_lock)
    get_lock_info = csrf_exempt(get_lock_info)
    clear_expired_locks = csrf_exempt(clear_expired_locks)
