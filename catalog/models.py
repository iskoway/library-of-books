from django.db import models
from django.urls import reverse


class Author(models.Model):
    full_name = models.CharField("Имя автора", max_length=150)
    biography = models.TextField("Биография", blank=True)

    class Meta:
        ordering = ["full_name"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return self.full_name


class Category(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    slug = models.SlugField("Slug", max_length=120, unique=True)
    description = models.TextField("Описание", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("catalog:category_books", args=[self.slug])


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Автор",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Категория",
    )
    published_year = models.PositiveIntegerField("Год издания", blank=True, null=True)
    description = models.TextField("Описание")
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse("catalog:book_detail", args=[self.pk])
