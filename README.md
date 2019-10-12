# Example on how to make things with Class Based Views

Longer explanation (pt-br) in [here](https://medium.com/@leportella/class-based-views-no-django-d76b01ed644e)

TLDR:
  * views.py exemplifies how to make things using Class Based Views
  * old_views.py exemplifies same urls but with functions



## Installation

This project was updated to Python 3.7


```
$ pip install -r my_library/requirements.txt
```


## Running the project

To run the server of the project you can use:

```
$ python my_library/manage.py runserver
```

You should apply migrations to the database, so we can have the tables we need:

```
$ python my_library/manage.py migrate
```


## URLs available


* admin/
* welcome/

Endpoints defined by `views.py`
* my-books/
* book-detail-by-id/<id>
* book-detail-by-code/<code>
* book-update/<pk>
* book-create
* author-create

Endpoints defined by `old_views.py`
* old/welcome/
* old/my-books/
* old/book-detail-by-id/<pk>
* old/book-detail-by-code/<code>
* old/book-update/<pk>

