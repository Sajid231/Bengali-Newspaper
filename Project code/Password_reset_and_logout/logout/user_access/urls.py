from django.urls import path
import user_access.views as UserView


urlpatterns = [
    # Logout Page
    path('logout/', UserView.LogoutView, name='Logout'),
]
