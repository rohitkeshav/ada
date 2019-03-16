from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    u_types = (
        ('owner', 'Owner')
        , ('tenant', 'Tenant')
    )

    middle_name = models.CharField(verbose_name='middle name', max_length=150, blank=True, null=True)
    user_type = models.CharField(choices=u_types, blank=False, null=False)

    def __str__(self):
        return self.email
