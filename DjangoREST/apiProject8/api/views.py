from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author, Book
from .serializers import AuthorSerializers, BookSerializers

@api_view(['GET'])
def all_books(request):
    book = Book.objects.all()
    serializer = BookSerializers(book, many=True)
    return Response(serializer.data)

#select_related to optimized foreign key 

@api_view(['GET'])
def select_book(request):
    book = Book.objects.select_related('author').all()
    serializer = BookSerializers(book, many=True)
    return Response(serializer.data)

#using prefetch_related to optimize reverse Foreign key relationships

@api_view(['GET'])
def prefetch_authors(request):
    author = Author.objects.prefetch_related('book').all()
    serializer = AuthorSerializers(author, many=True)
    return Response(serializer.data)    