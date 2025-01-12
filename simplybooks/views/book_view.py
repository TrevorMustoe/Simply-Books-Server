"""View module for handling requests about book """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooks.models import Book
from simplybooks.models import Author


class BookView(ViewSet):
    """Level up book  view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single book 

        Returns:
            Response -- JSON serialized book 
        """
        # Here we are getting a single book by the primary key (pk)  
        book = Book.objects.get(pk=pk)
        # sending it to our serializer to be converted to useable json
        serializer = BookSerializer(book)
        # then returing the serialzed data
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all book  

        Returns:
            Response -- JSON serialized list of book 
        """
        #Book is a variable stores the data accessed through our books model in this case we are accessing all of the data
        book = Book.objects.all()
        
        # This allows us to use query pararmams to be set for uid and favorite
        uid = request.query_params.get('uid', None)
        
        
        # Here we are checking if uid is set to anything other than None and if it is we are returning books filtered by this UID 
        # This totally works just make sure you have a / after your book in the request. 
        # example:
        # http://localhost:8000/book?uid=1
        if uid is not None:
            book = book.filter(uid=uid)
            
##############################################################################################################################################
#This is where we could add another statement that returns everthing else that is considered public since there is no UID present
#This would have to check if uid is set to None to return those books only. Then we can have a user set to public or private true or false if true it will display it to public if 
            
# We would first need to get all books of course
# Then we need to set a boolean statement on our books models 
# use an if statement to check if the boolean of public is set to false 
# if so maybe we could we return all the books that are set to false as well as only from the UID.
# if not, (set to true)---> (else), we would just return all books to the user and dont need to check for UID since its now public
# This feels messy but could work
##############################################################################################################################################
   
   
         #This is serializing the data and converting it to a json    
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        # Here I am 
        author = Author.objects.get(id=request.data["author"])

        book = Book.objects.create(
            author=author,
            uid=request.data["uid"],
            title=request.data["title"],
            image=request.data["image"],
            price=request.data["price"],
            sale=request.data["sale"],
            description=request.data["description"],
        )
        serializer = BookSerializer(book)
        return Response(serializer.data)
        
class BookSerializer(serializers.ModelSerializer):
    """JSON serializer for books
    """
    class Meta:
        model = Book
        fields = ('id', 'author','uid', 'title', 'image', 'price', 'sale', 'description')