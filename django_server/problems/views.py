from django.views.generic import View, DetailView

from django_server.problems.models import Problem, Solution


class ProblemDetailView(DetailView):
    context_object_name = 'problem'
    model = Problem
    pk_url_kwarg = 'id'

    template_name = 'problems/problem.html'
