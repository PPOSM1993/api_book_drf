from rest_framework import serializers
from .models import GenderBooks, Book


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderBooks
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'