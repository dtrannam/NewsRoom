from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Article, Author

def details(request, article_id):
    try:
        a = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'articles/details.html', {
        'article': a})

def new_authors(request):
    return render(request, 'articles/new_author.html')

def new_articles(request):
    authors = Author.objects.get_queryset()
    return render(request, 'articles/new_article.html', {"authors": authors})

def authors(request): 
    try:
        a = Author.objects.all()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'articles/authors.html', {
        'authors': a})
        
def home(request):
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    template = loader.get_template('articles/home.html')
    context = {
        'latest_articles': latest_articles
    }
    return HttpResponse(template.render(context, request))

def year(request, year):
    return HttpResponse("You are reviewing articles from %s" % year)

def created_author(request):
    print(request.POST)
    b = Author(name=request.POST["name"], email=request.POST["email"])
    b.save()
    return HttpResponseRedirect('/articles/authors/')