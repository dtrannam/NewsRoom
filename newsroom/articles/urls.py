from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("<int:article_id>", views.details, name='details'),
    path("year/<int:year>", views.year, name='year')
]