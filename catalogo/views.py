from django.shortcuts import render

# Create your views here.

from .models import Produto, Categoria

def list_produtos(request):
    contexto = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'catalogo/lista_produtos.html', contexto)


def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    contexto = {
        'categoria_atual': categoria,
        'list_produto': Produto.objects.filter(categoria=categoria),
    }
    return render(request, 'catalogo/categoria.html', contexto)


def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    contexto = {
        'produto' : produto,
    }
    return render(request, 'catalogo/produto.html', contexto)