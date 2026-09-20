from django.contrib import admin

# Importa duas ferramentas essenciais para criar rotas:
# 'path': Usada para definir uma URL específica.
# 'include': Usada para repassar a responsabilidade daquela URL para outro arquivo.
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # ROTAS DA SUA API (Agrupadas na versão 1)
    
    # O 'include' aqui é fantástico para a organização. Em vez de você escrever 
    # todas as 50 rotas do seu sistema neste único arquivo, você delega isso.
    # O comando diz: "Se a URL começar com 'api/v1/', vá até o arquivo 'urls.py' 
    # do aplicativo 'disclosure' (ou enterprise, etc) e veja o resto do caminho lá."
    path('api/v1/', include('disclosure.urls')),
    path('api/v1/', include('enterprise.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('review.urls')),

]
