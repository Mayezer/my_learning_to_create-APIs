# Importa as classes base de permissão do DRF
from rest_framework import permissions


# Cria uma classe de permissão GLOBAL. Em vez de criar uma classe para cada model
# (como ProductPermissionClass), essa descobre sozinha qual model está sendo acessado.
class GlobalDefaultPermission(permissions.BasePermission):

    # Método principal chamado pelo DRF para liberar ou bloquear o acesso
    def has_permission(self, request, view):

        # Chama a função interna para descobrir qual é o nome da permissão exigida
        # Exemplo do que ela tenta descobrir: "products.view_product" ou "users.add_user"
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        # Se não conseguiu descobrir a permissão (ex: a view não tem um 'queryset'), bloqueia o acesso
        if not model_permission_codename:
            return False

        # Se descobriu, pergunta ao Django se o usuário logado TEM essa permissão específica
        return request.user.has_perm(model_permission_codename)


    # Método privado (indicado pelos __) que monta o nome da permissão no padrão do Django
    def __get_model_permission_codename(self, method, view):
        try:
            # Pega o nome do model (ex: 'product') através do queryset da view
            model_name = view.queryset.model._meta.model_name

            # Pega o nome do app (ex: 'products') onde o model está (CORRIGIDO: era model_meta)
            app_label = view.queryset.model._meta.app_label

            # Pega a ação (view, add, change, delete) baseada no método HTTP (GET, POST, etc.)
            action = self.__get_action_sufix(method)

            # Junta tudo no formato exigido pelo Django: "nome_do_app.ação_nomedomodel"
            return f'{app_label}.{action}_{model_name}'

        # Se a view não tiver um 'queryset' configurado, vai dar erro de atributo.
        # Nesse caso, retorna None (o que causará o bloqueio do acesso lá no has_permission)
        except AttributeError:
            return None


    # Método privado que traduz o tipo de requisição HTTP para a palavra que o Django usa nas permissões
    def __get_action_sufix(self, method):
        # Dicionário de tradução (De-Para)
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'HEAD': 'view',
            'OPTIONS': 'view',
        }

        # Se o método não existir no dicionário, retorna uma string vazia
        return method_actions.get(method, '')
