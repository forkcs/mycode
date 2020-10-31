from django.db import models

from django_server.accounts.models import Account

LANGUAGES = (
    (1, 'Python'),
    (2, 'C++'),
)


class Problem(models.Model):
    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"

    teacher = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100_000)
    language = models.SmallIntegerField(choices=LANGUAGES)
    tests = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


PROBLEM_STATUSES = (
    (1, 'OK'),
    (2, 'Error'),
    (3, 'Pending'),
    (4, 'No Status')
)


class Solution(models.Model):
    class Meta:
        verbose_name = "Solution"
        verbose_name_plural = "Solutions"

    student = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    problem = models.ForeignKey(to=Problem, on_delete=models.CASCADE)
    text = models.CharField(max_length=100_000)
    status = models.SmallIntegerField(choices=PROBLEM_STATUSES, null=True, blank=True, default=4)
    score = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        pass
