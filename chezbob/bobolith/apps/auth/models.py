from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as DjangoGroup
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Represents a Chez Bob User.
    Inherits: username, email, is_staff, is_active,
              date_joined, password, last_login, and is_active.
    """
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)

    nickname = models.CharField(_('nickname'), max_length=255)

    balance = models.DecimalField(_('balance'), default=0, max_digits=12, decimal_places=2)

    is_fraudulent = models.BooleanField(_('fraudulent'), default=False)

    last_purchase = models.DateTimeField(_('last purchase'), blank=True, null=True)
    last_deposit = models.DateTimeField(_('last deposit'), blank=True, null=True)

    notes = models.TextField()

    # These are the fields required for, e.g. 'manage.py createsuperuser'.
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'nickname']

    def get_short_name(self):
        """Return the short name for the user."""
        return self.nickname


class Group(DjangoGroup):
    class Meta:
        proxy = True
