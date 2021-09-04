from django.urls import path
import threading
from news.views import ScrapeThreading, NewsView

urlpatterns = [
    path('news/', NewsView, name='news'),
]

# Initializing the threading of Scraping
threading.Thread(target=ScrapeThreading, daemon=True).start()       # daemon thread runs in background
