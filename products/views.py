from products.models import Product
import json # Módulo nativo do Python para converter entre JSON e tipos do Python (dicionários/listas).
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404


@method_decorator(csrf_exempt, name='dispatch') 
# method_decorator: Adapta um decorador de função para funcionar dentro de uma classe (Class-Based View).
# csrf_exempt: Desativa a verificação de token CSRF para permitir requisições de clientes externos (como APIs via POST).
class ProductView(View):
    # View: Classe base do Django que transforma nossa classe em uma view HTTP.

    def get(self, request): 
        # O Django executa o método com o nome do verbo HTTP correspondente (neste caso, GET).
        # Product.objects.all(): Busca todos os registros do modelo Product no banco de dados.
        # values(...): Seleciona apenas os campos especificados em vez de trazer o objeto completo.
        # list(...): Converte o QuerySet em uma lista Python para que possa ser serializada em JSON.
        # JsonResponse: Serializa os dados e retorna uma resposta HTTP com o header 'application/json'.
        
        products = Product.objects.all() 
        data = list(products.values('id', 'name', 'category', 'price', 'description')) 
        return JsonResponse(data, safe=False) 


    def post(self, request):
        # Método acionado automaticamente pelo Django em requisições POST.
        
        # request.body.decode('utf-8'): Decodifica os bytes brutos da requisição em texto formatado em UTF-8.
        # json.loads(...): Converte a string JSON em um dicionário Python manipulável.
        data = json.loads(request.body.decode('utf-8'))
        
        # Cria (com método create) a instância e já salva o registro diretamente no banco de dados
        new_product = Product.objects.create(
            name=data['name'],
            category=data['category'],
            price=data['price'],
            description=data['description']
        )
        
        # Monta os dados de retorno com as informações do item recém-criado
        response_data = {
            'id': new_product.id,
            'name': new_product.name,
            'message': "Produto criado com sucesso!"
        }
        
        # Retorna a confirmação em JSON com status HTTP 201 (Created)
        return JsonResponse(response_data, status=201)


@method_decorator(csrf_exempt, name='dispatch') 
# Define a classe da view (visualização). Ela herda de 'View' (uma classe base do Django), 
# o que permite lidar com requisições HTTP (como GET, POST) de forma estruturada.
class ProductDetailView(View):
    
    # Define o método acionado automaticamente em requisições HTTP do tipo GET (consultar/ler).
    # 'self': referencia a própria classe.
    # 'request': contém todos os dados da requisição HTTP.
    # 'pk' (Primary Key): é o ID do produto passado na URL (ex: /produtos/5/).
    def get(self, request, pk):
        # Tenta buscar no banco de dados um 'Product' com o ID (pk) passado.
        # Se o produto não existir, interrompe e retorna um erro HTTP 404 (Not Found) 
        # automaticamente, evitando que o sistema quebre.
        product = get_object_or_404(Product, pk=pk)
        # Cria um dicionário Python extraindo apenas os atributos que queremos 
        # retornar (neste caso, 'id' e 'name') do objeto produto encontrado.
        data = {
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'description': product.description,
            
        }
        
        # Converte o dicionário 'data' para o formato JSON e o devolve como 
        # resposta HTTP para o cliente. 
        # O resultado será algo como: {"id": 1, "name": "Produto Exemplo"}
        return JsonResponse(data)


    # O método 'put' é usado para atualizações completas de um registro.
    # Ele é acionado quando a API recebe uma requisição HTTP PUT.
    def put(self, request, pk):
        # Busca o produto existente no banco de dados (ou retorna 404)
        product = get_object_or_404(Product, pk=pk)
        
        # Tenta ler e converter os dados enviados. 
        # Em APIs, os dados do PUT/POST geralmente vêm no 'body' (corpo) da requisição em formato JSON.
        try:
            body_data = json.loads(request.body)
            
            # Atualiza os campos do produto com os novos dados recebidos.
            # Usamos body_data.get('name', product.name) para que, se o nome não for 
            # enviado na requisição, ele mantenha o nome antigo que já estava no banco.
            product.name = body_data.get('name', product.name)
            
            # Salva as alterações no banco de dados
            product.save()
            
            # Retorna o produto atualizado como confirmação de sucesso
            return JsonResponse({
                'id': product.id,
                'name': product.name,
                'category': product.category,
                'price': product.price,
                'description': product.description,
                
            })
            
        # Captura o erro caso o cliente envie um JSON malformado
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido.'}, status=400)


    # O método 'delete' é acionado quando a API recebe uma requisição HTTP DELETE.
    # Ele é usado especificamente para remover um registro.
    def delete(self, request, pk):
        
        # Busca o produto existente no banco de dados (retorna 404 se não achar)
        product = get_object_or_404(Product, pk=pk)
        
        # Executa o comando que apaga definitivamente o registro do banco
        product.delete()
        
        # Retorna uma resposta de sucesso.
        # Em APIs, após um DELETE, é comum retornar uma mensagem confirmando com status 200 (OK),
        # ou apenas um status 204 (No Content) sem corpo de texto.
        return JsonResponse({'message': 'Produto deletado com sucesso.'}, status=200)
