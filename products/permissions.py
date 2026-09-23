# Importa as classes base de permissão do Django REST Framework
from rest_framework import permissions

# Cria uma classe de permissão customizada herdando as regras base do DRF
class ProductPermissionClass(permissions.BasePermission):

    # Método principal que o DRF chama para decidir se o usuário pode acessar a rota
    def has_permission(self, request, view):
        
        # Se for uma requisição de leitura (GET, OPTIONS ou HEAD)...
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            # ...verifica se o usuário logado tem a permissão do Django para VER produtos
            return request.user.has_perm('products.view_product')

        # Se for uma requisição de criação (POST)...
        if request.method == 'POST':
            # ...verifica se o usuário tem permissão para ADICIONAR produtos
            return request.user.has_perm('products.add_product')

        # Se for uma requisição de atualização total (PUT) ou parcial (PATCH)...
        if request.method in ['PUT', 'PATCH']:
            # ...verifica se o usuário tem permissão para ALTERAR produtos
            return request.user.has_perm('products.change_product')

        # Se for uma requisição de exclusão (DELETE)...
        if request.method == 'DELETE':
            # ...verifica se o usuário tem permissão para DELETAR produtos
            return request.user.has_perm('products.delete_product')

        # Se não cair em nenhuma das regras acima, nega o acesso por padrão
        return False
