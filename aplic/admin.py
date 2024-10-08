from django.contrib import admin

from .models import Categoria, Prato, Pedido, PedidoPrato

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco')
    list_filter = ('categoria',)  # Permite filtrar por categorias
    search_fields = ('nome', 'descricao')
    ordering = ('categoria', 'nome')  # Ordenar por categoria e nome

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data')
    list_filter = ('data',)
    search_fields = ('cliente__username', 'cliente__email')
    date_hierarchy = 'data'  # Permite navegação por hierarquia de data

class PedidoPratoInline(admin.TabularInline):
    model = PedidoPrato
    extra = 1  # Quantidade de linhas extras para adicionar

class PedidoDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data')
    inlines = [PedidoPratoInline]  # Adiciona os itens de pedidos como linha
    list_filter = ('data',)
    search_fields = ('cliente__username',)
    ordering = ('-data',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Prato, PratoAdmin)
admin.site.register(Pedido, PedidoDetailAdmin)
