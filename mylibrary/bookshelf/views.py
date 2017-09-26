from django.views.generic import (DetailView, ListView, TemplateView,
                                  UpdateView)

from .forms import BookForm
from .models import Book


class WelcomeView(TemplateView):
    template_name = 'welcome.html'


class BooksView(ListView):
    model = Book
    template_name = 'my-books.html'


class BookDetailByIdView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'


class BookDetailByCodeView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'

    def get_object(self):
        return Book.objects.get(code=self.kwargs['code'])


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'my-book-edit.html'
    form_class = BookForm
    success_url = '/my-books'
