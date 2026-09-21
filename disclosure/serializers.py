from rest_framework import serializers
from disclosure.models import Disclosure


class DisclosureSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Disclosure
        fields = '__all__'

    # O DRF tem uma regra de ouro para nomes: se você criar uma função chamada 
    # 'validate_<nome_do_campo>', ele vai executá-la automaticamente quando 
    # receber dados para esse campo específico. 
    # Neste caso, ele está validando o campo 'release_date' (data de lançamento/divulgação).
    # O parâmetro 'value' é a data exata que o usuário enviou na requisição.
    def validate_release_date(self, value):
        
        # Aqui ele pega o ano da data enviada pelo usuário (value.year) e verifica 
        # se é menor que 2026.
        if value.year < 2020:
            
            # Se a data for de 2025 para trás, o sistema barra a requisição.
            # O DRF interrompe o salvamento no banco e devolve um erro HTTP 400 (Bad Request)
            # para o usuário, mostrando a mensagem exata escrita abaixo.
            raise serializers.ValidationError('O ano da divulgação não pode ser anterior a 2020.')
        
        # Se a data for de 2026 em diante, o código ignora o 'if' e chega nesta linha.
        # É OBRIGATÓRIO retornar o valor no final da validação para que o DRF 
        # continue o processo e salve o dado no banco de dados.
        return value
