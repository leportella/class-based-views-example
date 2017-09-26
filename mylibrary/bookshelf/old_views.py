from django.http import Http404
from django.shortcuts import render

from .forms import BookForm
from .models import Book


def edit_book(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        return render(request, 'my-book-edit.html')
    if request.method == 'POST':




def get_book(request, pk):

    if request.method == 'GET':
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        return render(request, 'my-book-detail.html', {object: book})
