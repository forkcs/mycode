from django.contrib import admin

from django_server.problems.models import Solution, Problem


admin.site.register(Problem, Solution)
