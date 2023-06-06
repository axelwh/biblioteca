from django.contrib import admin
from models import Autor, Libro, Editor


# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email',)
    search_fields = ('nombre', 'apellidos',)


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editor', 'fecha_de_publicacion',)
    list_filter = ('fecha_de_publicacion',)
    date_hierarchy = 'fecha_de_publicacion'
    ordering = ('-fecha_de_publicacion',)
    fields = ('titulo', 'autores', 'editor', 'portada',)
    filter_horizontal = ('autores',)
    raw_id_fields = ('editor',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Editor)
