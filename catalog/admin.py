from django.contrib import admin

from .models import Author, Book, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "book_count")
    search_fields = ("full_name",)

    @admin.display(description="Книг")
    def book_count(self, obj: Author) -> int:
        return obj.books.count()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "book_count")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

    @admin.display(description="Книг")
    def book_count(self, obj: Category) -> int:
        return obj.books.count()


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "published_year", "created_at")
    list_filter = ("category", "author")
    search_fields = ("title", "description", "author__full_name", "category__name")
