from django.db import models
from .book import Book
from .genre import Genre

  # Note that if this is not working to change the class name back to GenreBook and make new migrations
class Genre_Book(models.Model):
  # no need to add _id here since we are telling django that it is a FK it will do it automatically :)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    
    