from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from biblioteca.models import Libro, Autor, Editor
from forms import LibroForm, AutorForm, EditorForm


# Create your views here.
def read_editors(request):
    editors = Editor.objects.all()
    context = {
        "editors": editors,
        "url_names": {
            "update": 'biblioteca:update_editor',
            "delete": 'biblioteca:delete_editor',
        }
    }
    return render(request, 'biblioteca/editores/editores_list.html', context)


def create_editor(request):
    form = EditorForm()
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:read_editors')
    context = {
        'form': form
    }
    return render(request, 'biblioteca/editores/editores_create.html', context)


def update_editor(request, editor_id):
    # try:
    #     editor = Editor.objects.get(id=editor_id)
    # except Editor.DoesNotExist:
    #     raise Http404
    editor = get_object_or_404(Editor, id=editor_id)
    # editor.objects.prefetch_related('editor_libro')
    form = EditorForm(instance=editor)
    if request.method == 'POST':
        form = EditorForm(request.POST, instance=editor)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:read_editors')
    context = {
        'form': form
    }
    return render(request, 'biblioteca/editores/editores_create.html', context)


def delete_editor(request, editor_id):
    editor = Editor.objects.get(id=editor_id)
    if request.method == 'POST':
        editor.delete()
        return redirect('biblioteca:read_editors')
    context = {
        'editor': editor,
        'url_names': {
            'read_all': 'biblioteca:read_editors'
        }
    }
    return render(request, 'biblioteca/editores/editores_delete.html', context)


def read_authors(request):
    authors = Autor.objects.all()
    context = {
        "authors": authors,
        "url_names": {
            "update": 'biblioteca:update_author',
            "delete": 'biblioteca:delete_author',
        }
    }
    return render(request, 'biblioteca/autores/autores_list.html', context)


def create_author(request):
    form = AutorForm()
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:read_authors')
    context = {
        'form': form
    }
    return render(request, 'biblioteca/autores/autores_create.html', context)


def update_author(request, author_id):
    author = Autor.objects.get(id=author_id)
    form = AutorForm(instance=author)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:read_authors')
    context = {
        'form': form
    }
    return render(request, 'biblioteca/autores/autores_create.html', context)


def delete_author(request, author_id):
    author = Autor.objects.get(id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('biblioteca:read_authors')
    context = {
        'author': author,
        'url_names': {
            'read_all': 'biblioteca:read_authors'
        }
    }
    return render(request, 'biblioteca/autores/autores_delete.html', context)


def create_book(request):
    form = LibroForm()
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:read_books')
    context = {
        "form": form
    }
    return render(request, 'biblioteca/libros/libros_create.html', context)


def read_books(request):
    books = Libro.objects.all()
    print(books)
    context = {
        "books": books,
        "url_names": {
            "update": "biblioteca:update_book",
            "delete": "biblioteca:delete_book",
        }
    }
    return render(request, 'biblioteca/libros/libros_list.html', context)


def update_book(request, book_id):
    book = Libro.objects.get(id=book_id)
    form = LibroForm(instance=book)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('biblioteca:read_books')
    context = {
        'form': form
    }
    return render(request, 'biblioteca/libros/libros_create.html', context)


def delete_book(request, book_id):
    book = Libro.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('biblioteca:read_books')
    context = {
        'book': book,
        'url_names': {
            'read_all': 'biblioteca:read_books'
        }
    }
    return render(request, 'biblioteca/libros/libros_delete.html', context)


class EditoresReadAll(ListView):
    model = Editor
    template_name = 'biblioteca/editores/editores_list.html'

    def get_context_data(self, **kwargs):
        context = super(EditoresReadAll, self).get_context_data(**kwargs)
        editors = self.model.objects.all()
        context["editors"] = editors
        context["url_names"] = {
            "update": 'biblioteca:clases_update_editor',
            "delete": 'biblioteca:clases_delete_editor',
        }
        return context


class EditoresCreate(CreateView):
    model = Editor
    form_class = EditorForm
    template_name = 'biblioteca/editores/editores_create.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_editors')


class EditoresUpdate(UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = 'biblioteca/editores/editores_create.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_editors')


class EditoresDelete(DeleteView):
    model = Editor
    template_name = 'biblioteca/editores/editores_delete.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_editors')

    def get_context_data(self, **kwargs):
        context = super(EditoresDelete, self).get_context_data(**kwargs)
        editor_id = self.kwargs.get('pk')
        editor = self.model.objects.get(id=editor_id)
        context["editor"] = editor
        context["url_names"] = {
            'read_all': 'biblioteca:clases_read_all_editors'
        }
        return context


class AuthorReadAll(ListView):
    model = Autor
    template_name = 'biblioteca/autores/autores_list.html'

    def get_context_data(self, **kwargs):
        context = super(AuthorReadAll, self).get_context_data(**kwargs)
        authors = self.model.objects.all()
        context["authors"] = authors
        context["url_names"] = {
            "update": 'biblioteca:clases_update_author',
            "delete": 'biblioteca:clases_delete_author',
        }
        return context


class AuthorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autores/autores_create.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_author')


class AuthorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autores/autores_create.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_author')


class AuthorDelete(DeleteView):
    model = Autor
    template_name = 'biblioteca/autores/autores_delete.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_author')

    def get_context_data(self, **kwargs):
        context = super(AuthorDelete, self).get_context_data(**kwargs)
        author_id = self.kwargs.get('pk')
        author = self.model.objects.get(id=author_id)
        context["author"] = author
        context["url_names"] = {
            'read_all': 'biblioteca:clases_read_all_author'
        }
        return context


class BookReadAll(ListView):
    model = Libro
    template_name = 'biblioteca/libros/libros_list.html'

    def get_context_data(self, **kwargs):
        context = super(BookReadAll, self).get_context_data(**kwargs)
        books = self.model.objects.all()
        context["books"] = books
        context["url_names"] = {
            "update": 'biblioteca:clases_update_book',
            "delete": 'biblioteca:clases_delete_book',
        }
        return context


class BookCreate(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libros/libros_create.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_books')


class BookUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'biblioteca/libros/libros_create.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_books')


class BookDelete(DeleteView):
    model = Libro
    template_name = 'biblioteca/libros/libros_delete.html'
    success_url = reverse_lazy('biblioteca:clases_read_all_books')
    
    def get_template_names(self):
        return super(BookDelete, self).get_template_names()

    # def get_queryset(self):
    #     return self.queryset.all()
    #
    # def get_object(self, queryset=None):
    #     book_id = self.kwargs.get('pk')
    #     book = self.model.objects.get(id=book_id)
    #     return book
    #
    # """
    #
    #
    #     self.get_object
    #         foo = Libro.object.all()
    #         # ...
    #         foo = foo.get(id=10)
    #
    #         select * from libro where id=10;
    #
    #         if libre.name i != "":
    #
    #         self.get_queryset
    #             Libro.object.all() => select * from libro;
    #
    #             self.get
    #                 self.get_context_data
    #
    #                 dispatch
    # """

    def get_context_data(self, **kwargs):
        context = super(BookDelete, self).get_context_data(**kwargs)
        # book_id = self.kwargs.get('pk')
        # book = self.model.objects.get(id=book_id)
        context["book"] = self.object  # book
        context["url_names"] = {
            'read_all': 'biblioteca:clases_read_all_books'
        }
        return context
