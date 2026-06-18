from django.test import TestCase
from django.urls import reverse

from .models import Author, Book, Category


class CatalogViewsTests(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(full_name="Тестовый автор")
        self.category = Category.objects.create(name="Роман", slug="roman")
        self.book = Book.objects.create(
            title="Тестовая книга",
            author=self.author,
            category=self.category,
            published_year=2024,
            description="Описание книги",
        )

    def test_home_page_loads(self) -> None:
        response = self.client.get(reverse("catalog:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_search_filters_books(self) -> None:
        response = self.client.get(reverse("catalog:book_list"), {"q": "Тестовая"})
        self.assertContains(response, self.book.title)

    def test_create_book(self) -> None:
        response = self.client.post(
            reverse("catalog:book_create"),
            {
                "title": "Новая книга",
                "author": self.author.pk,
                "category": self.category.pk,
                "published_year": 2025,
                "description": "Новое описание",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(title="Новая книга").exists())
