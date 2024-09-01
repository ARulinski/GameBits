from django.urls import path
from . import views
from .views import profile_view, UpdateProfileView, DeleteProfileView

urlpatterns = [
    path("login_view", views.login_view, name="login_view"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("register_view", views.register_view, name="register_view"),
    path('profile_view', profile_view.as_view(), name='profile_view'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('delete_profile/', DeleteProfileView.as_view(), name='delete_profile'),
    
]