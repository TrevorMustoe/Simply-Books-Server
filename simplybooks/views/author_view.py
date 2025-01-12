"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooks.models import Author


class AuthorView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_types = Author.objects.all()
        serializer = AuthorSerializer(game_types, many=True)
        return Response(serializer.data)
        
class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for authors
    """
    class Meta:
        model = Author
        fields = ('email', 'uid', 'first_name', 'last_name', 'image', 'favorite')