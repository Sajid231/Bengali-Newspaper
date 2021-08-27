from django.urls import path, include

urlpatterns = [
    # Include User_access App url
    path('', include('user_access.urls')),
]
