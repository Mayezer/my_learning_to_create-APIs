# Importa as views genéricas, a view base (APIView) e os status HTTP do DRF
from rest_framework import generics, views, status
from rest_framework.response import Response # Necessário para retornar os dados na APIView

# Importa as funções de agregação do banco de dados do Django (Contagem e Média)
from django.db.models import Count, Avg

# Importa a permissão nativa que exige que o usuário esteja logado (com token válido)
from rest_framework.permissions import IsAuthenticated

# Importa as classes do seu próprio projeto (Permissões, Models e Serializers)
from products.permissions import ProductPermissionClass
from products.models import Product
from products.serializers import ProductSerializers
from review.models import Review


# -------------------------------------------------------------------------
# View para LISTAR (vários produtos) e CRIAR (um novo produto)
# -------------------------------------------------------------------------
class ProductListCreateView(generics.ListCreateAPIView):
    # generics.ListCreateAPIView: View genérica pronta para lidar com:
    # - GET: Retorna a lista de produtos.
    # - POST: Cria um novo produto.

    permission_classes = (IsAuthenticated, ProductPermissionClass,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


# -------------------------------------------------------------------------
# View para LER (um único produto), ATUALIZAR e DELETAR
# -------------------------------------------------------------------------
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # generics.RetrieveUpdateDestroyAPIView: View genérica pronta para lidar com UM item específico (via ID):
    # - GET (Retrieve): Detalhes de um produto.
    # - PUT / PATCH (Update): Atualiza o produto.
    # - DELETE (Destroy): Apaga o produto.

    permission_classes = (IsAuthenticated, ProductPermissionClass,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


# -------------------------------------------------------------------------
# View CUSTOMIZADA para exibir ESTATÍSTICAS dos produtos e avaliações
# -------------------------------------------------------------------------
class ProductStatsView(views.APIView):
    # views.APIView: É a view mais básica do DRF. Diferente das genéricas acima, 
    # ela não faz nada sozinha. Você precisa escrever manualmente o que acontece no GET, POST, etc.

    # Exige usuário logado e com permissões adequadas
    permission_classes = (IsAuthenticated, ProductPermissionClass,)
    
    # O queryset é definido aqui para ser usado abaixo e também para manter a compatibilidade
    # com classes de permissão dinâmicas (como a GlobalDefaultPermission que fizemos antes)
    queryset = Product.objects.all()

    # Define exatamente o que acontece quando o usuário fizer uma requisição GET nesta rota
    def get(self, request):
        
        # 1. Conta o total de produtos cadastrados no banco
        total_products = self.queryset.count()
        
        # 2. Agrupa os produtos pelo campo 'product__name' (ou equivalente) e conta quantos existem em cada grupo
        products_by_enterprise = self.queryset.values('product__name').annotate(count=Count('id'))
        
        # 3. Conta o total de avaliações (Reviews) feitas
        total_reviews = Review.objects.count()
        
        # 4. Calcula a média (Avg) da coluna 'stars' das avaliações. 
        # O ['avg_stars'] no final extrai apenas o número do dicionário que o Django retorna.
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        # Retorna um JSON montado manualmente com todas as estatísticas calculadas
        return Response(
            data={
                'total_products': total_products,
                'products_by_enterprise': products_by_enterprise,
                'total_reviews': total_reviews,
                # Arredonda a média para 1 casa decimal. Se não houver avaliações (None), retorna 0.
                'average_stars': round(average_stars, 1) if average_stars else 0,
            },
            status=status.HTTP_200_OK # Define o status HTTP como 200 (Sucesso)
        )

    def post(self, request):
        ...

    def delete(self, request):
        ...