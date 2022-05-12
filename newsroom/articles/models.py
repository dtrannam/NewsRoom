from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)

    def has_views(self):
        return views > 0

    def __str__(self):
        return self.title
