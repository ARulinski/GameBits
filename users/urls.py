from django.urls import path
from . import views

urlpatterns = [
    path("login_view", views.login_view, name="login_view"),
    path("logout_user", views.logout_user, name="logout_user"),
]