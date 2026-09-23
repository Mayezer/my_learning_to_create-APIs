# Importa as views genéricas do DRF que já vêm com os métodos HTTP prontos
from rest_framework import generics

# Importa a permissão nativa que exige que o usuário esteja logado (com token válido)
from rest_framework.permissions import IsAuthenticated

# Importa as classes do seu próprio projeto (Permissões, Models e Serializers)
from products.permissions import ProductPermissionClass
from products.models import Product
from products.serializers import ProductSerializers


# -------------------------------------------------------------------------
# View para LISTAR (vários produtos) e CRIAR (um novo produto)
# -------------------------------------------------------------------------
class ProductListCreateView(generics.ListCreateAPIView):
    # generics.ListCreateAPIView: View genérica pronta para lidar com:
    # - GET: Retorna a lista de produtos.
    # - POST: Cria um novo produto.

    # Define as regras de acesso para esta rota:
    # 1. IsAuthenticated: O usuário PRECISA enviar um token JWT válido (estar logado).
    # 2. ProductPermissionClass: O usuário precisa ter as permissões específicas do Django (view_product, add_product).
    permission_classes = (IsAuthenticated, ProductPermissionClass,)

    # Define de onde os dados serão buscados (O queryset base)
    queryset = Product.objects.all()

    # Define o "tradutor" (Serializador)
    # Converte os objetos do banco para JSON (na resposta do GET) e JSON para objetos (no envio do POST)
    serializer_class = ProductSerializers


# -------------------------------------------------------------------------
# View para LER (um único produto), ATUALIZAR e DELETAR
# -------------------------------------------------------------------------
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # generics.RetrieveUpdateDestroyAPIView: View genérica pronta para lidar com UM item específico (via ID):
    # - GET (Retrieve): Detalhes de um produto.
    # - PUT / PATCH (Update): Atualiza o produto.
    # - DELETE (Destroy): Apaga o produto.

    # Aplica as mesmas regras de segurança: Usuário logado + Permissões específicas (change_product, delete_product)
    permission_classes = (IsAuthenticated, ProductPermissionClass,)

    # O queryset base. O DRF vai pegar essa lista e buscar automaticamente o produto pelo ID passado na URL
    queryset = Product.objects.all()

    # Define o mesmo serializador para fazer a tradução dos dados desta view
    serializer_class = ProductSerializers
