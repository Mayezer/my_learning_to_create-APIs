from django.db import models
from products.models import Product
from enterprise.models import Enterprise


SOCIAL_NETWORK_CHOICES = (
    ('INSTAGRAM', 'Instagram'),
    ('FACEBOOK', 'Facebook'),
    ('YOUTUBE', 'Youtube'),
    ('TIK_TOK', 'Tik Tok'),
    ('X', 'X'),
    ('WHATSAPP', 'Whatsapp'),
    ('KAWAI', 'Kawai'),
)

class Disclosure(models.Model):
    social_network = models.CharField(
        max_length=100,
        choices=SOCIAL_NETWORK_CHOICES
    )
    date = models.DateField(blank=True, null=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='products',
        null=True,
        blank=True
    )

    enterprise = models.ManyToManyField(Enterprise, related_name='enterprises')

    def __str__(self):
        return self.social_network
