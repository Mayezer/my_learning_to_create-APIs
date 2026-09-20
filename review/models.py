from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='reviews',
        null=True,
        blank=True
    )

    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avaliação não pdoe ser menor que 0 estrelas!'),
            MaxValueValidator(5, 'Avaliação não pode ser maior que 5 estrelas!')
        ]
    )

    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Review de {self.stars} estrelas para {self.product}"
