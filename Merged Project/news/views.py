import threading
import time
from news.models import News
from news.scrape import Scrape
from django.shortcuts import render


# Web scrape threading
def ScrapeThreading():
    t1 = threading.Thread(target=Scrape, daemon=True)       # daemon thread runs in background
    t1.start()
    time.sleep(600)
    ScrapeThreading()


# Show News to user
def NewsView(request):
    search = request.GET.get('search')

    if search is None or bool(search) == False:
        result = News.objects.order_by('-time')[:30]
        number = result.count()

    else:
        print(search)
        result = News.objects.filter(heading__icontains=search).order_by('-time')[:30]
        number = result.count()

    data = {
        'news': result,
        'number': number,
    }
    return render(request, 'news.html', data)
