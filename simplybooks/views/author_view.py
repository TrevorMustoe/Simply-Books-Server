"""View module for handling requests about author """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooks.models import Author


class AuthorView(ViewSet):
    """Level up author s view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single author 

        Returns:
            Response -- JSON serialized author 
        """
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all author 

        Returns:
            Response -- JSON serialized list of author 
        """
        author = Author.objects.all()
        
        uid = request.query_params.get('uid', None)
        
        
        # Here we are checking if uid is set to anything other than None and if it is we are returning books filtered by this UID 
        # This totally works just make sure you have a / after your book in the request. 
        # example:
        # http://localhost:8000/book?uid=1
        if uid is not None:
            author = author.filter(uid=uid)
            #This is where we could add another statement that returns everthing else that is considereed "public since there is no UID present"
            
            
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        author = Author.objects.create(
            email=request.data["email"],
            uid=request.data["uid"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            image=request.data["image"],
            favorite=request.data["favorite"],
        )
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
        
class AuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for authors
    """
    class Meta:
        model = Author
        fields = ('email', 'uid', 'first_name', 'last_name', 'image', 'favorite')