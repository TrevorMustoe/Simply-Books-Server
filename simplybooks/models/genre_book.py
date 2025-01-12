from django.db import models
from .book import Book
from .genre import Genre

class Genre_Book(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    
    