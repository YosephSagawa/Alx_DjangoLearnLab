from rest_framework import serializers
from .models import Book, Author

# This serializer is used to serialize the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__" #Includes all the fields to be serialized and represented in JSON format

    def validate(self, data): #Makes sure pulication year is not in the future
        if(data['publication_year'] > 2025):
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return data

# This serializer is used to serialize the Author Model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) #Boook serializer is used to serialize the Book model
    class Meta:
        model = Author
        fields = ["name", "books"] #Includes name field and also books associated with the author to be represented

