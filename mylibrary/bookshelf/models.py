from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=250)
    pages = models.IntegerField()
    code = models.IntegerField()
