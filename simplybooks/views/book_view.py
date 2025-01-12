"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooks.models import Book


class BookView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_types = Book.objects.all()
        serializer = BookSerializer(game_types, many=True)
        return Response(serializer.data)
        
class BookSerializer(serializers.ModelSerializer):
    """JSON serializer for books
    """
    class Meta:
        model = Book
        fields = ('id', 'author','uid', 'title', 'image', 'price', 'sale', 'description')