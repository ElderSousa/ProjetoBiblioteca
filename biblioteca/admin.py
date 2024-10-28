from django.contrib import admin
from biblioteca.models import Livro, Locador, Locacao

class Livros(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'isbn')
    list_display_links = ('id', 'isbn')
    search_fields = ('ibs', )

admin.site.register(Livro, Livros)

class Locadores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'tipo_locador')
    list_display_links = ('id', )
    search_fields = ('id', )

admin.site.register(Locador, Locadores)

class Locacoes(admin.ModelAdmin):
    list_display = ('id', 'livro', 'locador', 'periodo')
    list_display_links = ('id', )
    search_fields = ('id', )

admin.site.register(Locacao, Locacoes)
