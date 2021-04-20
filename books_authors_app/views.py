from django.shortcuts import render,redirect
from .models import Book, author


def index(request):

    context = {
        'books': Book.objects.all()
    }

    return render(request,'index.html',context)

def add_book(request):
    form = request.POST

    Book.objects.create(
        title=form['title'],
        desc=form['description']
    )

    return redirect('/')

def add_book_to_author(request, author_id):
    this_author = author.objects.get(id=author_id)
    add_book = Book.objects.get(id=request.POST['book_id'])

    this_author.books.add(add_book)

    return redirect(f'/author/{author_id}')


def authors(request):

    context = {
        'authors': author.objects.all()
    }

    return render(request, 'authors.html',context)

def add_author(request):

    form=request.POST

    author.objects.create(
        first_name = form['first_name'],
        last_name = form['last_name'],
        note = form['note']
    )

    return redirect('/authors')


def add_author_to_book(request, book_id):
    add_books = Book.objects.get(id=book_id)
    add_author = author.objects.get(id=request.POST['author_id'])

    add_books.authors.add(add_author)

    return redirect(f'/books/{book_id}')


def author_info(request, author_id):
    context = {
        'author': author.objects.get(id=author_id),
        'books': Book.objects.all()
    }

    return render(request,'author-info.html',context)

def single_book(request, book_id):
    context = {
        'books': Book.objects.get(id=book_id),
        'authors': author.objects.all()
    }

    return render(request, 'book-info.html',context)
