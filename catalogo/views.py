from django.shortcuts import render

# Create your views here.

from .models import Produto, Categoria

def list_produtos(request):
    contexto = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'catalogo/lista_produtos.html', contexto)