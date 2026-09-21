# Importa o módulo de serializadores (serializers) do Django REST Framework.
# Os serializadores têm duas funções principais:
# 1. Transformar objetos complexos do Python (como os dados do Banco de Dados) em JSON.
# 2. Fazer o caminho inverso: receber um JSON (do usuário) e transformar em um formato que o Python entenda para salvar no banco.
from rest_framework import serializers

# Importa o modelo 'Product' do arquivo models.py do aplicativo 'products'.
# O modelo é a representação da sua tabela no banco de dados.
from products.models import Product


# Cria a classe do seu serializador, herdando de 'serializers.ModelSerializer'.
# O ModelSerializer é um "atalho mágico" do DRF. Em vez de você ter que 
# recriar cada campo na mão (texto, número, data), ele olha para o seu modelo 
# e cria tudo automaticamente, incluindo as regras de validação.
class ProductSerializers(serializers.ModelSerializer):

    # A classe 'Meta' é uma classe interna usada no Django para passar 
    # configurações (metadados) para a classe "pai" (ProductSerializers).
    class Meta:
        
        # Diz ao serializador qual é o modelo que ele deve usar como base.
        # Aqui, estamos amarrando o serializador à tabela 'Product'.
        model = Product
        
        # Define quais campos do modelo devem aparecer na sua API (no JSON).
        # O valor '__all__' é um atalho que diz: "Pegue absolutamente TODOS os 
        # campos que existem no modelo Product (id, nome, preço, descrição, etc) 
        # e coloque na API". 
        # *Nota: Se você quisesse exibir apenas o nome e o preço, você usaria uma 
        # lista assim: fields = ['nome', 'preco']
        fields = '__all__'

    # A intenção aqui é criar uma função que o DRF rode automaticamente 
    # quando receber os dados do campo 'description'.
    # O 'value' é o texto que o usuário digitou na descrição.
    def validate_description(self, value):
        
        # A função len() conta o tamanho (length) de algo. 
        # Aqui, ela está contando quantos caracteres (letras, espaços, números) 
        # o texto digitado possui. Se for maior que 500...
        if len(value) > 500:
            
            # ... o DRF levanta um erro, bloqueia o salvamento e devolve essa 
            # mensagem para o usuário.
            raise serializers.ValidationError('A descrição não pode ter maior que 500 caracteres.')
        
        # Se o texto tiver 500 caracteres ou menos, ele passa direto pelo 'if'
        # e a função retorna o valor validado para que ele seja salvo no banco.
        return value
