from django.urls import path

from . import views


app_name = "catalog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("books/add/", views.BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("categories/<slug:slug>/", views.CategoryBooksView.as_view(), name="category_books"),
]
