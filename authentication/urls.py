from django.urls import path
# Importa as views do SimpleJWT para gerar, atualizar e verificar os tokens
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    # Rota para GERAR o token.
    # O usuário envia login/senha e recebe um "access token" e um "refresh token".
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain-pair'),

    # Rota para ATUALIZAR o token.
    # Recebe o "refresh token" (quando o "access token" expira) e devolve um novo "access token" válido.
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rota para VERIFICAR o token.
    # Recebe um token e apenas checa se ele é válido (retorna 200 OK) ou se já expirou/é inválido.
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
