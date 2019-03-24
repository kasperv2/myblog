
from django.shortcuts import render, get_object_or_404
from news.models import News

from django.http import HttpResponse
# Create your views here.


# Create your views here.
def news_list(request):
    """Вывод всех новостей
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})

def index(request):
    return render(request,'news/hello.html')


def new_single(request, pk):
	new = get_object_or_404(News,id=pk)
	return render(request, "news/new_single.html", {"new":new})