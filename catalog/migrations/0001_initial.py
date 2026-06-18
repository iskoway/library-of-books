from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=150, verbose_name="Имя автора")),
                ("biography", models.TextField(blank=True, verbose_name="Биография")),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
                "ordering": ["full_name"],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="Название")),
                ("slug", models.SlugField(max_length=120, unique=True, verbose_name="Slug")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Название")),
                ("published_year", models.PositiveIntegerField(blank=True, null=True, verbose_name="Год издания")),
                ("description", models.TextField(verbose_name="Описание")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Создано")),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="books", to="catalog.author", verbose_name="Автор")),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="books", to="catalog.category", verbose_name="Категория")),
            ],
            options={
                "verbose_name": "Книга",
                "verbose_name_plural": "Книги",
                "ordering": ["title"],
            },
        ),
    ]
