from django.views.generic import View, DetailView

from django_server.problems.models import Problem, Solution


class ProblemDetailView(DetailView):
    context_object_name = 'problem'
    model = Problem

    template_name = 'problems/problem.html'
