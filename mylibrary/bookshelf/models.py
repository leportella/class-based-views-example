from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
       return self.name


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=250)
    pages = models.IntegerField()
    code = models.IntegerField()

    def __str__(self):
        return '%s - %s - %s - %s' % (self.author.name, self.title, self.code, self.pages)
