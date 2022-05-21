from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("<int:article_id>/", views.details, name='details'),
    path("year/<int:year>/", views.year, name='year'),
    path("authors/", views.authors, name="author"),
    path("authors/new/", views.new_authors, name="new_authors"),
    path("authors/created/", views.created_author, name="created_author"),
    path("new/", views.new_articles, name="new_articles")
]