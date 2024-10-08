from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Prato, Pedido, PedidoPrato


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'restaurante/listar_categorias.html', {'categorias': categorias})


def listar_pratos_por_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(id=categoria_id)
    except Categoria.DoesNotExist:
        return HttpResponse('Categoria não encontrada', status=404)

    pratos = Prato.objects.filter(categoria=categoria)
    return render(request, 'restaurante/listar_pratos.html', {'categoria': categoria, 'pratos': pratos})


def detalhes_prato(request, prato_id):
    try:
        prato = Prato.objects.get(id=prato_id)
    except Prato.DoesNotExist:
        return HttpResponse('Prato não encontrado', status=404)

    return render(request, 'restaurante/detalhes_prato.html', {'prato': prato})


def fazer_pedido(request):
    if request.method == 'POST':
        cliente = request.user
        itens = request.POST.getlist('itens')  # Lista de pratos selecionados pelo cliente
        if not itens:
            return HttpResponse('Nenhum item selecionado', status=400)

        pedido = Pedido.objects.create(cliente=cliente)
        for item_id in itens:
            try:
                prato = Prato.objects.get(id=item_id)
            except Prato.DoesNotExist:
                return HttpResponse(f'Prato com ID {item_id} não encontrado', status=404)

            quantidade = int(request.POST.get(f'quantidade_{item_id}', 1))
            PedidoPrato.objects.create(pedido=pedido, prato=prato, quantidade=quantidade)

        return HttpResponse('Pedido realizado com sucesso!')

    return render(request, 'restaurante/fazer_pedido.html')


def listar_pedidos(request):
    cliente = request.user
    pedidos = Pedido.objects.filter(cliente=cliente)
    return render(request, 'restaurante/listar_pedidos.html', {'pedidos': pedidos})


def detalhes_pedido(request, pedido_id):
    try:
        pedido = Pedido.objects.get(id=pedido_id)
    except Pedido.DoesNotExist:
        return HttpResponse('Pedido não encontrado', status=404)

    itens_pedido = PedidoPrato.objects.filter(pedido=pedido)
    return render(request, 'restaurante/detalhes_pedido.html', {'pedido': pedido, 'itens_pedido': itens_pedido})
