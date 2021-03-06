from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

# Create your views here.


def book_list(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "totalB": num_books,
        "avgR": avg_rating
    })


def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_details.html", {
        "book": book
    })
