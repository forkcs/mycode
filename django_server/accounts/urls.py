from django.urls import path

from django_server.accounts.views import LogInView, LogOutView, RegisterView


urlpatterns = [
    path('login/', LogInView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('register/', RegisterView.as_view()),
]
