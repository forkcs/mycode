from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

ACCOUNT_TYPES = (
    (1, 'Admin'),
    (2, 'Teacher'),
    (3, 'Student')
)


class Account(models.Model):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    account_type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    school_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name
