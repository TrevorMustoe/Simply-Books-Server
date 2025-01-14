from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooks.models import Genre_Book
from simplybooks.models import Genre
from simplybooks.models import Book


class Genre_Book_View(ViewSet):
  
  # GENRES ARE NOT LOCKED BEHIND UIDS BECAUSE THEY WILL BE PROVIDED BY SIMPLY BOOKS AND NOT EDITABLE BY THE USERS

    def retrieve(self, request, pk):
      try:
          genre_book = Genre_Book.objects.get(pk=pk)
          serializer = Genre_BookSerializer(genre_book)
          return Response(serializer.data)
      except Genre_Book.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
      try:
        genre_book = Genre_Book.objects.all()
    
        serializer = Genre_BookSerializer(genre_book, many=True)
        return Response(serializer.data)
      except:
        return Response({'message': 'Check query'}, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):
      book = Book.objects.get(pk=request.data["book"])
      genre = Genre.objects.get(pk=request.data["genre"])

      genre_book = Genre_Book.objects.create(
          book=book,
          genre=genre,
      )
      serializer = Genre_BookSerializer(genre_book)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
      book = Book.objects.get(pk=request.data["book"])
      genre = Genre.objects.get(pk=request.data["genre"])
      
      genre_book = Genre_Book.objects.get(pk=pk)
      genre_book.book = book
      genre_book.genre = genre

      genre_book.save()

      serializer = Genre_BookSerializer(genre_book)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
      genre_book = Genre_Book.objects.get(pk=pk)
      genre_book.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)


class Genre_BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre_Book
        fields = ('id', 'book', 'genre' )
        depth = 1