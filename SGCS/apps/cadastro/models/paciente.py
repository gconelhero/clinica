from django.db import models

from decimal import Decimal

from .base import Pessoa


TIPO_PACIENTE = [
    ('Particular', 'Particular'),
    ('Prefeitura', 'Prefeitura'),
    ('Convenio', 'Convênio'),
]


class Paciente(Pessoa):
    tipo = models.CharField(max_length=20, choices=TIPO_PACIENTE, default='Particular', null=True, blank=True)
    data_entrada = models.DateField(null=True, blank=True)
    limite_de_credito = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'), null=True, blank=True)
    desativar = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Paciente"