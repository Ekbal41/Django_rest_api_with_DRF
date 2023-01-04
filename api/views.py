# ---------------------------------------------------------------------------
# from django.shortcuts import render
# from .models import Book
# from django.http import JsonResponse
# from rest_framework.response import Response
# from .serializer import BookSerializer
# from rest_framework.decorators import api_view
# from rest_framework import status
#
#
# # Create your views here.
#
# @api_view(['GET'])
# def all_book(requets):
#     try:
#         books = Book.objects.all()  # Complex data
#     except:
#         return Response({
#             "Erorr" : "No book available",
#         },status=status.HTTP_404_NOT_FOUND)
#     # pythonBooks = list(books.values())  # pythonic data
#     # return JsonResponse({
#     #    "books": pythonBooks
#     # })
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def create_book(request):
#     book = BookSerializer(data=request.data)
#     if book.is_valid():
#         book.save()
#         return Response(book.data)
#     else:
#         return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['DELETE', 'PUT', 'GET'])
# def book(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response({
#             "Erorr": "Book not found",
#         },status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         s = BookSerializer(book)
#         return Response(s.data)
#
#     if request.method == "PUT":
#
#         s = BookSerializer(book, data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "DELETE":
#         book.delete()
#         return Response({
#             "delete": True,
#         }, status=status.HTTP_404_NOT_FOUND)

# ------------------------------------------------------------------------------------------------
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer


class Books(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if token:
            try:
                books = Book.objects.all()  # Complex data
            except:
                return Response({
                    "Erorr": "No book available",
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            raise AuthenticationFailed('Unauthenticated!')

    def post(self, request):
        token = request.COOKIES.get('jwt')
        if token:
            book = BookSerializer(data=request.data)
            if book.is_valid():
                book.save()
                return Response(book.data)
            else:
                return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise AuthenticationFailed('Unauthenticated!')


class Update(APIView):

    def get_book_by_pk(self, pk):
        book = Book.objects.get(pk=pk)
        return book

    def put(self, request, pk):
        token = request.COOKIES.get('jwt')
        if token:
            book = self.get_book_by_pk(pk)
            s = BookSerializer(book, data=request.data)
            if s.is_valid():
                s.save()
                return Response(s.data)
            else:
                return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise AuthenticationFailed('Unauthenticated!')

    def get(self, request, pk):
        token = request.COOKIES.get('jwt')
        if token:
            book = book = self.get_book_by_pk(pk)
            s = BookSerializer(book)
            return Response(s.data)
        else:
            raise AuthenticationFailed('Unauthenticated!')

    def delete(self, request, pk):
        token = request.COOKIES.get('jwt')
        if token:
            book = book = self.get_book_by_pk(pk)
            book.delete()
            return Response({
                "delete": True,
            }, status=status.HTTP_404_NOT_FOUND)
        else:
            raise AuthenticationFailed('Unauthenticated!')
# -----------------------------------------------------------------------------------------------