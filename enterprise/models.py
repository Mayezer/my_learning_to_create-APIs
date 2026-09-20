# Importa o módulo 'models' do Django, que contém todas as ferramentas 
# necessárias para criar as tabelas do banco de dados usando código Python (ORM).
from django.db import models

# Define uma tupla (lista que não muda) com as opções disponíveis para a região.
# O padrão do Django para 'choices' é usar pares: ('Valor_no_Banco', 'Nome_na_Tela')
# 1º valor (ex: 'REGION_NORTH'): É o que será de fato salvo no Banco de Dados.
# 2º valor (ex: 'Norte'): É o que vai aparecer para o usuário ver e selecionar (no Admin, formulários, etc).
REGION_CHOICES = (
    ('REGION_NORTH', 'Norte'),
    ('REGION_NORTH_EAST', 'Nordeste'),
    ('REGION_CENTRAL_WEST', 'Centro-Oeste'),
    ('REGION_SOUTHEAST', 'Sudeste'),
    ('REGION_SOUTH', 'Sul'),
)

# Cria a classe 'Enterprise' (Empresa), que herda de 'models.Model'.
# Ao herdar de models.Model, o Django entende que esta classe deve virar 
# uma tabela no banco de dados chamada "enterprise".
class Enterprise(models.Model):
    
    # Cria uma coluna na tabela chamada 'name' (nome).
    # models.CharField: Indica que o campo é para textos (strings).
    # max_length=200: É obrigatório em CharField e diz que o nome pode ter no máximo 200 caracteres.
    name = models.CharField(max_length=200)
    
    # Cria uma coluna na tabela chamada 'region' (região).
    region = models.CharField(
        max_length=100,           # Tamanho máximo do texto no banco (100 caracteres é suficiente para as opções acima).
        choices=REGION_CHOICES,   # Trava este campo: o banco só aceita os valores definidos na lista REGION_CHOICES.
        blank=True,               # Regra para formulários: permite que o campo fique vazio (não é obrigatório preencher na tela).
        null=True                 # Regra para o Banco de Dados: permite salvar essa coluna como "NULL" (vazia) lá no banco.
    )
    
    # Método mágico do Python que define como um objeto dessa classe deve "se apresentar" em texto.
    # Se você não colocar isso, ao listar as empresas no Django Admin, elas aparecerão 
    # como "Enterprise object (1)", "Enterprise object (2)".
    # Com esse método, elas aparecerão com o nome salvo (ex: "Minha Empresa LTDA").
    def __str__(self):
        return self.name
