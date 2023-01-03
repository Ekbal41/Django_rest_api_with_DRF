from django.urls import path
# from .views import all_book, create_book, book
from .views import Books,Update

urlpatterns = [

    # path('', all_book, name="all_book"),
    # path('create', create_book, name="create_book"),
    # path('book/<int:pk>', book, name="book")
    path("", Books.as_view()),
    path("book/<int:pk>", Update.as_view())

]
