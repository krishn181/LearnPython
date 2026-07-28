from rest_framework import serializers
from .models import Author, Book

class BookSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializers(serializers.ModelSerializer):
    book = BookSerializers(many = True, read_only=True)
    class Meta:
        model = Author
        fields = ['id','name','book']

