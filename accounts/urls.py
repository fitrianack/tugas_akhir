# accounts/urls.py
from django.urls import path
from django.contrib.auth import views
from accounts.forms import UserLoginForm
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        'login/',
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    )
]
