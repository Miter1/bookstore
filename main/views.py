from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from datetime import date
from .forms import *
# Create your views here.
# 'request' is an object that contains request data,
# views function should return response object
# def index(request):
    # print('test')
    # return HttpResponse('Greetings from Django!')
# def index(request):
#     # Create an Author object:
#     author = Author()
#     # Assigning it's attributes values
#     author.first_name = 'John'
#     author.last_name = 'Johnson'
#     author.biography = 'Honest life...'
#     author.birth_date = date(1980,5,5)
#     # Save an Author model to the database:
#     author.save()
#     return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')
""" 
A view function should receive a request object 
and return a response object. 
Request object holds data of your request.
Response object holds data of server response to your request.
"""
def add_author(request):
    if request.method == 'POST':
        # if request.method == 'POST' and 'test' in request.POST:
        #     print('test')
        print('POST data:', request.POST)

        # Creating a form object, with a POST data:
        form = AuthorForm(request.POST)

        # Check if form is valid and if so, saving the corresponding
        # model to a database:
        if form.is_valid():
            form.save()
            # redirect(): redirects to url by it's name
            return redirect('index')
    else:
        print('request GET data', request.GET)

        form = AuthorForm()
    
    # Passing a request object to a 'render' function
    # Passing a html template to be rendered in a browser
    # Passing a template context, which is a dictionary
    return render(request, 'add-author.html', {'form': form})


def show_authors(request):
    # Get all Author objects
    authors = Author.objects.all()
    print(authors)
    # Passing authors QuerySet to the template
    return render(request, 'show-authors.html', {'authors' : authors})


def show_books(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'show-books.html', {'books' : books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'add-book.html', {'form': form})

def delete_author(request, author_id):
    Author.objects.get(id=author_id).delete()
    return redirect('show-authors')

def delete_authors(request):
    Author.objects.all().delete()
    return redirect('show-authors')

def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('show-books')

def delete_books(request):
    Book.objects.all().delete()
    return redirect('show-books')


        
def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'show-author.html',{'author': author})

def show_book(request, book_id):
    book = Book.objects.get(id = book_id)
    return render(request, 'show-book.html',{'book':book})

def edit_author(request, author_id):
    author = Author.objects.get(id = author_id)
    if request.method == 'POST' :
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('show-authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'edit-author.html', {'form': form, 'author_id' : author_id})

def edit_book(request, book_id):
    book = Book.objects.get(id = book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show-books')
    else:
        form = BookForm(instance=book)
    return render(request,'edit-book.html', {'form' : form, 'book_id' :book_id})

def send_letter(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LetterForm()
    return render(request, 'send-letter.html', {'form' : form})

def send_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-books')
    else:
        form = ReviewForm()
    return render(request, 'send-review.html', {'form' : form})