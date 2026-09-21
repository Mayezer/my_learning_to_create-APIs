from rest_framework import serializers
# Importa a função Avg do Django.
# Avg significa "Average" (média) e é usada para calcular
# a média de valores diretamente no banco de dados.
from django.db.models import Avg
from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


    # Método responsável por calcular o valor do campo "rate".
    #
    # O nome precisa ser "get_rate" porque o campo criado acima
    # se chama "rate".
    #
    # obj representa o objeto Review que está sendo serializado.
    def get_rate(self, obj):

        # Verifica se essa Review possui um Product relacionado.
        #
        # No seu model, product aceita:
        # null=True
        # blank=True
        #
        # Portanto, é possível existir uma Review sem produto.
        if obj.product is None:

            # Se não houver produto relacionado, não existe como
            # calcular a média das avaliações desse produto.
            return None


        # obj
        # representa a Review atual.
        #
        # obj.product
        # acessa o Product relacionado com essa Review.
        #
        # obj.product.reviews
        # acessa todas as Reviews daquele Product.
        #
        # Isso funciona porque no seu ForeignKey você definiu:
        #
        # related_name='reviews'
        #
        # aggregate(...)
        # executa uma operação de agregação no banco de dados.
        #
        # Avg('stars')
        # calcula a média do campo "stars".
        #
        # average=Avg('stars')
        # cria o nome "average" para o resultado da média.
        #
        # O resultado do aggregate será parecido com:
        #
        # {
        #     'average': 4.333333333
        # }
        average = obj.product.reviews.aggregate(
            average=Avg('stars')
        )['average']

        # ['average']
        # pega somente o valor da chave "average".
        #
        # Portanto, ao invés de:
        #
        # {
        #     'average': 4.333333333
        # }
        #
        # a variável average ficará apenas com:
        #
        # 4.333333333


        # Verifica se realmente existe uma média.
        #
        # Quando não existem avaliações, o Avg() pode retornar None.
        if average is not None:

            # Arredonda a média para uma casa decimal.
            #
            # Exemplo:
            #
            # 4.333333333
            #
            # vira:
            #
            # 4.3
            return round(average, 1)


        # Caso não exista nenhuma avaliação para calcular a média,
        # retorna None.
        return None
