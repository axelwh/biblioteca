from django.conf.urls import url
from biblioteca import views

editor_functions_crud = [
    url(r'^editores/crear$', views.create_editor, name='create_editor'),
    url(r'^editores$', views.read_editors, name='read_editors'),
    url(r'^editores/(?P<editor_id>\d+)/update$', views.update_editor, name='update_editor'),
    url(r'^editores/(?P<editor_id>\d+)/delete$', views.delete_editor, name='delete_editor'),
]
editor_clases_crud = [
    url(r'^editores/clases/crear$', views.EditoresCreate.as_view(), name='clases_create_editor'),
    url(r'^editores/clases$', views.EditoresReadAll.as_view(), name='clases_read_all_editors'),
    url(r'^editores/clases/(?P<pk>\d+)/update$', views.EditoresUpdate.as_view(), name='clases_update_editor'),
    url(r'^editores/clases/(?P<pk>\d+)/delete$', views.EditoresDelete.as_view(), name='clases_delete_editor'),
]
author_functions_crud = [
    url(r'^autores/crear$', views.create_author, name='create_author'),
    url(r'^autores$', views.read_authors, name='read_authors'),
    url(r'^autores/(?P<author_id>\d+)/update$', views.update_author, name='update_author'),
    url(r'^autores/(?P<author_id>\d+)/delete$', views.delete_author, name='delete_author'),
]
author_clases_crud = [
    url(r'^autores/clases/crear$', views.AuthorCreate.as_view(), name='clases_create_author'),
    url(r'^autores/clases$', views.AuthorReadAll.as_view(), name='clases_read_all_author'),
    url(r'^autores/clases/(?P<pk>\d+)/update$', views.AuthorUpdate.as_view(), name='clases_update_author'),
    url(r'^autores/clases/(?P<pk>\d+)/delete$', views.AuthorDelete.as_view(), name='clases_delete_author'),
]
book_functions_crud = [
    url(r'^libros/crear$', views.create_book, name='create_book'),
    url(r'^libros$', views.read_books, name='read_books'),
    url(r'^libros/(?P<book_id>\d+)/update$', views.update_book, name='update_book'),
    url(r'^libros/(?P<book_id>\d+)/delete/$', views.delete_book, name='delete_book'),
]
book_clases_crud = [
    url(r'^libros/clases/crear$', views.BookCreate.as_view(), name='clases_create_book'),
    url(r'^libros/clases$', views.BookReadAll.as_view(), name='clases_read_all_books'),
    url(r'^libros/clases/(?P<pk>\d+)/update', views.BookUpdate.as_view(), name='clases_update_book'),
    url(r'^libros/clases/(?P<pk>\d+)/delete$', views.BookDelete.as_view(), name='clases_delete_book'),
]

editor_urls = editor_functions_crud + editor_clases_crud
author_urls = author_functions_crud + author_clases_crud
book_urls = book_functions_crud + book_clases_crud

urlpatterns = editor_urls + author_urls + book_urls
