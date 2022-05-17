from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader
from .models import Article, Author

def details(request, article_id):
    try:
        a = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'articles/details.html', {
        'article': a})

def home(request):
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    template = loader.get_template('articles/home.html')
    context = {
        'latest_articles': latest_articles
    }
    return HttpResponse(template.render(context, request))

def year(request, year):
    return HttpResponse("You are reviewing articles from %s" % year)