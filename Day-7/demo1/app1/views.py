from django.shortcuts import render
from .models import Books
# Create your views here.

def index(request):
    if request.method == "POST":
        author_name = request.POST['name']
        book = request.POST['book']
        email = request.POST['email']
        books = Books(auth_name = author_name, email=email, book_name=book)
        books.save()
        props = {'name': author_name, 'book': book, 'email': email}
        return render(request, 'index.html', props)
    return render(request, 'index.html')