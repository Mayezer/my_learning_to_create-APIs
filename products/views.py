# Importações presumidas (geralmente necessárias para este código funcionar)
# from rest_framework import generics
# from .models import Product
# from .serializers import ProductSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from products.serializers import ProductSerializers


# -------------------------------------------------------------------------
# View para LISTAR (vários produtos) e CRIAR (um novo produto)
# -------------------------------------------------------------------------
class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    # generics.ListCreateAPIView: É uma view genérica do Django REST Framework.
    # Ela já vem pronta para lidar com duas requisições HTTP:
    # 1. GET: Retorna uma lista de todos os itens.
    # 2. POST: Recebe dados e cria um novo item no banco de dados.
    
    # Define a consulta no banco de dados. 
    # Diz para a view: "Quando alguém fizer um GET, busque TODOS os produtos".
    queryset = Product.objects.all()
    
    # Define o arquivo de tradução (Serializador).
    # Diz para a view: "Use o ProductSerializers para converter os objetos do 
    # banco de dados em JSON (para quem pediu) e para converter o JSON que 
    # chega (via POST) em um objeto do banco de dados".
    serializer_class = ProductSerializers


# -------------------------------------------------------------------------
# View para LER (um único produto), ATUALIZAR e DELETAR
# -------------------------------------------------------------------------
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # generics.RetrieveUpdateDestroyAPIView: Outra view genérica do DRF.
    # Ela lida com as requisições HTTP focadas em UM item específico (usando o ID):
    # 1. GET (Retrieve): Retorna os detalhes de um único produto.
    # 2. PUT / PATCH (Update): Atualiza os dados de um produto existente.
    # 3. DELETE (Destroy): Apaga o produto do banco de dados.

    permission_classes = (IsAuthenticated,)

    # Define a base de busca. Mesmo sendo para um item só, a view precisa 
    # saber em qual "caixa" (tabela) procurar o item pelo ID na hora da requisição.
    queryset = Product.objects.all()
    
    # ADICIONADO: Assim como na classe de cima, esta view também precisa do 
    # serializador para traduzir as informações entre Banco de Dados <-> JSON.
    serializer_class = ProductSerializers
