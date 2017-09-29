from django.http import Http404
from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book


def welcome(request):
    return render(request, 'welcome.html')


def get_books_list(request):
    books = Book.objects.all()
    return render(request, 'my-books.html', {'object_list': books})


def get_book_by_id(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        return render(request, 'my-book-detail.html', {'object': book})


def get_book_by_code(request, code):
    if request.method == 'GET':
        try:
            book = Book.objects.get(code=code)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
            return render(request, 'my-book-detail.html', {'object': book})


def edit_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'my-book-edit.html', {'form': form, 'object': book})

    if request.method == 'POST':
        book = Book.objects.get(id=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/old/my-books')

