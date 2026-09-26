# 1. IMAGEM BASE
# Define o sistema operacional e a linguagem base do seu container.
# Aqui, pegamos a imagem oficial do Python, versão 3.14.4.
# O sufixo "-slim" indica uma versão mais limpa e leve do sistema, sem arquivos inúteis.
FROM python:3.14.4-slim

# 2. DIRETÓRIO DE TRABALHO
# Cria a pasta "/app" dentro do container.
# A partir deste momento, o Docker executa todos os próximos comandos dentro desta pasta.
WORKDIR /app

# 3. VARIÁVEIS DE AMBIENTE
# Impede que o Python crie arquivos de cache compilados (.pyc).
ENV PYTHONDONTWRITEBYTECODE 1
# Garante que os logs e erros do Python apareçam no terminal na mesma hora, sem atrasos.
ENV PYTHONUNBUFFERED 1

# 4. COPIAR ARQUIVOS
# O primeiro ponto (.) significa "tudo que está na pasta atual do meu computador".
# O segundo ponto (.) significa "para a pasta atual do container (que é a /app)".
# Resumo: Copia o código do seu projeto para dentro do container.
COPY . .

# 5. INSTALAÇÃO DE DEPENDÊNCIAS
# RUN executa comandos no terminal do container DURANTE a criação da imagem.
# Primeiro, atualizamos o 'pip' (gerenciador de pacotes do Python) para a versão mais recente.
RUN pip install --upgrade pip

# Em seguida, lemos o requirements.txt e instalamos as bibliotecas listadas lá.
# A flag "-r" é obrigatória para indicar que estamos lendo um arquivo.
RUN pip install -r requirements.txt

# 6. PREPARAÇÃO DO BANCO DE DADOS
# Está commitado pois agora usando o banco de dados PostgreSQL em container.
# RUN python manage.py migrate

# 7. EXPOSIÇÃO DE PORTA
# É apenas uma documentação. Avisa ao Docker que a aplicação lá dentro vai funcionar na porta 8000.
# Para acessarmos pelo navegador, precisamos mapear a porta do container para a porta do nosso computador.
EXPOSE 8000

# 8. COMANDO DE INICIALIZAÇÃO
# CMD é o comando principal e só é executado QUANDO o container for iniciado (em tempo de execução).
# O "&&" serve para encadear comandos: ele primeiro executa as migrações (agora sim o banco Postgres está acessível) 
# e, se der tudo certo, ele liga o servidor do Django permitindo o acesso externo ("0.0.0.0").
CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
