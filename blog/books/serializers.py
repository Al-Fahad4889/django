from rest_framework import serializers
from .models import Book,Author,Publisher
from datetime import datetime,timedelta
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def validate(self, attrs):
        description = attrs.get("description")
        publication_date = attrs.get("publication_date")
        price = attrs.get("price")

        # Validate title: Must be under 100 characters
        if attrs.get("title") and len(attrs["title"]) > 100:
            raise serializers.ValidationError("Title cannot exceed 100 characters.")

        # Validate description: Must have at least 10 words
        if description and len(description.split()) < 10:
            raise serializers.ValidationError("Description must have at least 10 words.")

        # Validate publication_date: Must be at least 1 month old
        if publication_date:
            one_month_ago = datetime.now().date() - timedelta(days=30)
            if publication_date > one_month_ago:
                raise serializers.ValidationError("Publication date must be at least 1 month old.")

        # Validate price: Must be between 100 and 10,000
        if price is not None and (price < 100 or price > 10000):
            raise serializers.ValidationError("Price must be between 100 and 10,000.")

        return attrs

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  # You can also specify specific fields as a list

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'