from django.urls import path

from django_server.problems.views import ProblemDetailView


urlpatterns = [
    path('detail/', ProblemDetailView.as_view())
]
