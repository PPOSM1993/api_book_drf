from django.shortcuts import render
from rest_framework import status
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.


#FORMA 1 de crear una API con Django Rest Framework, mediante funciones (def nombre funcion)
"""@api_view(['GET'])
def GenderBookList(request):
    gender_books = GenderBooks.objects.all()
    serializer = GenderSerializer(gender_books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def GenderBookCreate(request):
    serializer = GenderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response (serializer.errors)

@api_view(['POST'])
def BookCreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)"""


class GenderBookList(APIView):
    def get(self, request):
        gender_books = GenderBooks.objects.all()
        serializer = GenderSerializer(gender_books, many=True)
        return Response(serializer.data)

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class GenderBookCreate(APIView):
    def post(self, request):
        serializer = GenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)

class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)

class GenderBookDetail(APIView):
    def get_gender_by_pk(self, pk):
        try:
            return GenderBooks.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        gender_books = self.get_gender_by_pk(pk)
        serializer = GenderSerializer(gender_books)
        return Response(serializer.data)
    
    def put(self, request, pk):
        gender_books = self.get_gender_by_pk(pk)
        serializer = GenderSerializer(gender_books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gender_books = self.get_gender_by_pk(pk)
        gender_books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookDetail(APIView):

    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        books = self.get_book_by_pk(pk)
        serializer = BookSerializer(books)
        return Response(serializer.data)
    
    def put(self, request, pk):
        books = self.get_book_by_pk(pk)
        serializer = BookSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        books = self.get_book_by_pk(pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)