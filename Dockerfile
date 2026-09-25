# 1. IMAGEM BASE
# Define qual sistema operacional e ambiente inicial o seu container vai usar.
# Aqui, estamos pegando uma imagem oficial do Python na versão 3.14.4. 
# O sufixo "-slim" significa que é uma versão mais leve e enxuta do sistema.
FROM python:3.14.4-slim

# 2. DIRETÓRIO DE TRABALHO
# Cria a pasta "/learning_docker" dentro do container e avisa o Docker:
# "A partir de agora, execute todos os próximos comandos dentro desta pasta".
WORKDIR /app

# 3. COPIAR ARQUIVOS
# O primeiro ponto (.) significa "tudo que está na pasta atual do meu computador".
# O segundo ponto (.) significa "para a pasta atual do container (que é a /learning_docker)".
# Resumo: Copia o código do seu projeto para dentro do container.
COPY . .

# 4. INSTALAÇÃO DE DEPENDÊNCIAS
# RUN executa comandos no terminal do container DURANTE a criação da imagem.
# Primeiro, atualizamos o 'pip' (gerenciador de pacotes do Python) para a versão mais recente.
RUN pip install --upgrade pip

# Depois, lemos o arquivo requirements.txt e instalamos todas as bibliotecas listadas lá (ex: Django, DRF, etc).
# CORRIGIDO: Adicionei o "-r" que é obrigatório para ler arquivos.
RUN pip install -r requirements.txt

# 5. PREPARAÇÃO DO PROJETO
# Executa as migrações do Django, criando as tabelas no banco de dados.
# (Atenção: Em produção, geralmente fazemos isso fora do Dockerfile, mas para aprendizado/testes locais é comum).
RUN python manage.py migrate

# 6. EXPOSIÇÃO DE PORTA
# É apenas uma documentação. Avisa ao Docker que a aplicação lá dentro vai funcionar na porta 8000.
# Par acessa devemos fazer o espelhamento, pois a porta 8000 é a do conteiner não a do nosso computador
EXPOSE 8000

# 7. COMANDO DE INICIALIZAÇÃO
# CMD é o comando principal. Diferente do RUN (que roda na construção da imagem), 
# o CMD só é executado QUANDO o container for iniciado.
# Aqui, ele liga o servidor do Django e o "0.0.0.0" permite que ele seja acessado de fora do container.
CMD python3 manage.py runserver 0.0.0.0:8000
