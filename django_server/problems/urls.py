from django.urls import path

from django_server.problems.views import ProblemDetailView


urlpatterns = [
    path('<int:pk>/', ProblemDetailView.as_view())
]
