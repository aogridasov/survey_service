from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'auth'

urlpatterns = [
    path(
        'signup/',
        views.SignUp.as_view(template_name='users/signup.html'),
        name='signup'
    ),
    path(
        'logout/',
        LogoutView.as_view(next_page='surveys:index'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        '<int:user_id>/bback/',
        views.buy_background,
        name='buy_background'
    ),
    path(
        '<int:user_id>/bborder/',
        views.buy_border,
        name='buy_border'
    ),
]
