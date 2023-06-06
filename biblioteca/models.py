from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellidos = models.CharField(max_length=40, verbose_name='Apellidos')
    email = models.EmailField(blank=True, verbose_name='E-mail')

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)


class Libro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    autores = models.ManyToManyField(Autor, verbose_name='Autores')
    editor = models.ForeignKey(Editor, verbose_name='Editor', related_name='editor_libro')
    fecha_de_publicacion = models.DateField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas', editable=True)

    def __str__(self):
        return self.titulo
