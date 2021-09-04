from django.conf.urls import url
from django.urls import path
import user_access.views as UserView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Sign Up Page
    path('signup/', UserView.SignUpView, name='Signup'),
    # Login Page
    path('login/', UserView.LoginView, name='Login'),
    # Logout Page
    path('logout/', UserView.LogoutView, name='Logout'),

    # Password Reset Pages
    url(r'^password_reset/$', UserView.PasswordResetView, name='Password Reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
