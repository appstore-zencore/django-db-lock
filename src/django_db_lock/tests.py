import time
import json
from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy as reverse
from .services import acquire_lock as do_acquire_lock
from .services import release_lock as do_release_lock
from .services import get_lock_info as do_get_lock_info


class TestDjangoDbLock(TestCase):

    def setUp(self):
        self.url_acquire_lock = reverse("django_db_lock.acquire_lock")
        self.url_release_lock = reverse("django_db_lock.release_lock")
        self.url_get_lock_info = reverse("django_db_lock.get_lock_info")
        self.url_clear_expired_locks = reverse("django_db_lock.clear_expired_locks")

    def test01(self):
        assert do_acquire_lock("lock01", "worker01", 100)
        assert do_acquire_lock("lock01", "worker01", 100) == False
        assert do_release_lock("lock01", "worker01")

    def test02(self):
        assert do_acquire_lock("lock01", "worker01", 1)
        time.sleep(2)
        assert do_acquire_lock("lock01", "worker01", 1)

    def test03(self):
        assert do_acquire_lock("lock01", "worker01", 100)
        assert do_release_lock("lock01", "worker01")
        assert do_release_lock("lock01", "worker01")

    def test04(self):
        do_acquire_lock("lock01", "worker01", 100)
        info = do_get_lock_info("lock01")
        assert info["lock_name"] == "lock01"
        assert info["worker_name"] == "worker01"

    def test05(self):
        browser = Client()
        response = browser.post(self.url_acquire_lock, {"lock_name": "lock01", "worker_name": "worker01", "timeout": 300})
        data = json.loads(response.content.decode("utf-8"))
        assert data["result"]

        response = browser.post(self.url_acquire_lock, {"lock_name": "lock01", "worker_name": "worker01", "timeout": 300})
        data = json.loads(response.content.decode("utf-8"))
        assert data["result"] is False

        response = browser.get(self.url_get_lock_info, {"lock_name": "lock01"})
        data = json.loads(response.content.decode("utf-8"))
        assert data["result"]
        assert data["result"]["lock_name"] == "lock01"

        response = browser.post(self.url_release_lock, {"lock_name": "lock01", "worker_name": "worker01"})
        data = json.loads(response.content.decode("utf-8"))
        assert data["result"]

    def test06(self):
        browser = Client()
        response = browser.get(self.url_clear_expired_locks)
        data = json.loads(response.content.decode("utf-8"))
        assert data["result"]
