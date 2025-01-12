from django.db import models
from .author import Author

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    uid = models.CharField(max_length=30)
    title = models.CharField(max_length=55)
    image = models.URLField(max_length=12)
    price = models.IntegerField()
    sale = models.BooleanField()
    description = models.CharField(max_length=55)
  



# NOTES FROM ISSUE TICKET: 
# author_id (foreign key to Author, required): Associates the book with a specific author.
# firebaseKey (varchar, required): A unique identifier for the book in Firebase.
# title (string, required): The title of the book.
# image (URL field, optional): A URL pointing to an image of the book.
# price (integer, required): The price of the book in cents (or preferred currency unit).
# sale (boolean, default false): Indicates if the book is on sale.
# uid (string, required): The unique user ID associated with the book.
# description (text, optional): A detailed description of the book.