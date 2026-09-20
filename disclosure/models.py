# Importa as ferramentas de banco de dados do Django.
from django.db import models

# Importa as classes Product e Enterprise de outros aplicativos do seu projeto.
# Isso é necessário para criar vínculos entre esta tabela e as tabelas de Produto e Empresa.
from products.models import Product
from enterprise.models import Enterprise

# Define as opções de redes sociais.
# O 1º valor é o código salvo no banco, o 2º é o nome amigável exibido nas telas e formulários.
SOCIAL_NETWORK_CHOICES = (
    ('INSTAGRAM', 'Instagram'),
    ('FACEBOOK', 'Facebook'),
    ('YOUTUBE', 'Youtube'),
    ('TIK_TOK', 'Tik Tok'),
    ('X', 'X'),
    ('WHATSAPP', 'Whatsapp'),
    ('KAWAI', 'Kawai'),
)

# Cria a tabela 'Disclosure' (Divulgação) no banco de dados.
class Disclosure(models.Model):
    
    # Coluna para registrar a rede social.
    # É obrigatório (pois não tem blank/null) e restrito apenas às opções da lista acima.
    social_network = models.CharField(
        max_length=100,
        choices=SOCIAL_NETWORK_CHOICES
    )
    
    # Coluna para registrar uma data (apenas dia/mês/ano, sem horas).
    # É um campo opcional tanto no preenchimento das telas (blank) quanto no banco (null).
    date = models.DateField(blank=True, null=True)

    # RELACIONAMENTO "1 PARA MUITOS" (ForeignKey)
    # Significa: "Esta divulgação está vinculada a UM único produto, 
    # mas o mesmo produto pode ter VÁRIAS divulgações diferentes".
    product = models.ForeignKey(
        Product,
        # PROTECT: Regra de segurança importante! Se alguém tentar deletar um produto no banco 
        # e ele estiver vinculado a esta divulgação, o Django vai dar um erro e bloquear a exclusão.
        on_delete=models.PROTECT,
        # related_name: É o nome do "caminho de volta". Permite que você acesse as divulgações 
        # a partir de um objeto Produto. 
        related_name='products',
        # A divulgação pode ser salva sem nenhum produto atrelado (opcional).
        null=True,
        blank=True
    )

    # RELACIONAMENTO "MUITOS PARA MUITOS" (ManyToManyField)
    # Significa: "Uma única divulgação pode envolver VÁRIAS empresas, 
    # e uma única empresa pode estar em VÁRIAS divulgações".
    # O Django automaticamente criará uma tabela invisível no banco para gerenciar essa união.
    enterprise = models.ManyToManyField(
        Enterprise, 
        # Caminho de volta a partir da Empresa.
        related_name='enterprises'
    )

    # Método mágico do Python que define como o objeto aparece como texto.
    # No Django Admin, ao invés de "Disclosure object (1)", aparecerá o nome da 
    # rede social, por exemplo: "INSTAGRAM" ou "YOUTUBE".
    def __str__(self):
        return self.social_network
