from django.db import models

class Product(models.Model): # Criamos nossos campos para o nosso JSON.
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    
    def __str__(self): # Retorna o nome bem formatado em nossas buscas.
        return self.name
