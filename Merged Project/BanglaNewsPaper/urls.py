from django.urls import path, include
from django.views.generic import TemplateView
from news import urls as news_urls

urlpatterns = [

    # Home Page
    path('', TemplateView.as_view(template_name="index.html"), name="Index"),
    # News Page
    path('', include('news.urls')),
    # User functionality
    path('', include('user_access.urls')),
]
