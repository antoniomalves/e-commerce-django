# coding=utf-8

from django.db import models

# Create your models here.

class Categoria(models.Model):

    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Produto(models.Model):

    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    categoria = models.ForeignKey('catalogo.Categoria', verbose_name='Categoria')
    descricao = models.TextField('Descricao', blank=True)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def __str__(self):
        return self.nome