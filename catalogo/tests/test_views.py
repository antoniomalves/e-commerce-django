# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy

from catalogo.models import Produto, Categoria


class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalogo:list_produtos')
        self.client = Client()
        self.produtos = mommy.make('catalogo.Produto', _quantity=10)

    def tearDown(self):
        Produto.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo/lista_produtos.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('produtos' in response.context)
        list_produtos = response.context['produtos']
        self.assertEquals(list_produtos.count(), 10)