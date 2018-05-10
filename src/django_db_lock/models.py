from django.db import models
from django.utils.translation import ugettext_lazy as _


class Lock(models.Model):
    lock_name = models.CharField(max_length=32, unique=True)
    worker_name = models.CharField(max_length=32)
    lock_time = models.DateTimeField(auto_now_add=True)
    expire_time = models.DateTimeField()

    class Meta:
        verbose_name = _("Lock")
        verbose_name_plural = _("Locks")

    def __str__(self):
        return self.lock_name
