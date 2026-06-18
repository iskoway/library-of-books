from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "category", "published_year", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Например, Атомные привычки"}),
            "published_year": forms.NumberInput(attrs={"placeholder": "2024"}),
            "description": forms.Textarea(
                attrs={"rows": 5, "placeholder": "Краткое описание книги"}
            ),
        }
