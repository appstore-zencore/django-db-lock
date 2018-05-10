django-db-lock
==============

Lock something and keep status in database.


Install
-------

::

    pip install django-db-lock


Settings
--------

::

    INSTALLED_APPS = [
        ...
        'django_db_lock',
        ...
    ]


Use inside project
------------------

::

    import uuid
    from django_db_lock import acquire_lock
    from django_db_lock import release_lock

    def view01(request):
        lock_name = "view01lock"
        worker_name = str(uuid.uuid4())
        timeout = 10
        locked = acquire_lock(lock_name, worker_name, timeout)
        if locked:
            try:
                ....
            finally:
                release_lock(lock_name, worker_name)
        ...

Use outout project
------------------

::

    import requests

    def view02(request):
        data = {
            "lock_name": "view02lock",
            "worker_name": str(uuid.uuid4()),
            "timeout": 10,
        }
        response = request.post("http://api.server/system/dblock/acquire-lock", data=data)
        if response["result"]:
            try:
                ....
            finally:
                request.post("http://api.server/system/dblock/acquire-lock", data=data)
        ...

Install LockAdmin in admin site
-------------------------------

Add **REGISTER_DJANGO_DB_LOCK_ADMIN = True** in settings.py will register LockAdmin in django's default admin site.
