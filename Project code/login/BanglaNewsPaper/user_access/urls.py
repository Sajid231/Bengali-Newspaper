from django.urls import path
import user_access.views as UserView

urlpatterns = [
    # Login Page
    path('login/', UserView.LoginView, name='Login'),
]

