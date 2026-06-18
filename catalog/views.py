from django.contrib import messages
from django.db.models import Count, Q
from django.views.generic import CreateView, DetailView, ListView

from .forms import BookForm
from .models import Book, Category


class CatalogContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.annotate(book_total=Count("books"))
        context["search_query"] = self.request.GET.get("q", "").strip()
        return context


class HomeView(CatalogContextMixin, ListView):
    model = Book
    template_name = "catalog/home.html"
    context_object_name = "books"
    paginate_by = 6

    def get_queryset(self):
        return (
            Book.objects.select_related("author", "category")
            .order_by("-created_at")[:6]
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_categories"] = context["categories"][:4]
        context["total_books"] = Book.objects.count()
        return context


class BookListView(CatalogContextMixin, ListView):
    model = Book
    template_name = "catalog/book_list.html"
    context_object_name = "books"
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get("q", "").strip()
        queryset = Book.objects.select_related("author", "category")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(author__full_name__icontains=query)
                | Q(category__name__icontains=query)
            )
        return queryset


class CategoryBooksView(BookListView):
    template_name = "catalog/category_books.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.category = Category.objects.get(slug=self.kwargs["slug"])
        return queryset.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_category"] = self.category
        return context


class BookDetailView(CatalogContextMixin, DetailView):
    model = Book
    template_name = "catalog/book_detail.html"
    context_object_name = "book"


class BookCreateView(CatalogContextMixin, CreateView):
    form_class = BookForm
    template_name = "catalog/book_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Книга успешно добавлена в каталог.")
        return super().form_valid(form)
