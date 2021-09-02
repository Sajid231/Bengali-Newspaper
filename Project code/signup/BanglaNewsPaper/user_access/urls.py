from django.urls import path
import user_access.views as UserView

urlpatterns = [
    # Sign Up Page
    path('signup/', UserView.SignUpView, name='Signup'),
]

