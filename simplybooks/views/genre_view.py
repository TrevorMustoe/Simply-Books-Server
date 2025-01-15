"""View module for handling requests about genre """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooks.models import Genre


class GenreView(ViewSet):
    """Level up genre s view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single genre 

        Returns:
            Response -- JSON serialized genre 
        """
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all genre 

        Returns:
            Response -- JSON serialized list of genre 
        """
        genre = Genre.objects.all()
            
            
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        genre = Genre.objects.create(
            genre_name=request.data["genre_name"]
        )
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a book"""

        # Fetch the book to be updated
        genre = Genre.objects.get(pk=pk)

    

        # Update book details
        genre.genre_name = request.data["genre_name"]
        genre.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genres
    """
    class Meta:
        model = Genre
        fields = ('genre_name',)